create database leetcode;

/* 1378. Replace Employee ID With The Unique Identifier */
select unique_id,
       name
    from Employees e
    left outer join EmployeeUNI i
    on e.id = i.id


/* 1350. Students With Invalid Departments */
select s.id,s.name
    from Students s
    left outer join Departments d
    on s.department_id = d.id
    where d.name is null


/* 1068. Product Sales Analysis I */
select product_name,
       year,
       price
    from Product p
    left outer join Sales s
    on p.product_id = s.product_id
    where price is not null


/* 1303. Find the Team Size */
select employee_id,
       counts as team_size
    from Employee e
    left outer join
    (select team_id, 
        count(*) as counts 
        from Employee
        group by team_id
     ) s
     on e.team_id = s.team_id


/* 1069. Product Sales Analysis II */
select product_id, 
       sum(quantity) as total_quantity
     from Sales
     group by product_id


/* 1251. Average Selling Price */
select u.product_id, 
       round(sum(u.units* p.price)/sum(u.units),2) as average_price
    from UnitsSold u
    left outer join Prices p
    on u.product_id = p.product_id 
    and u.purchase_date between p.start_date and p.end_date
    group by product_id


/* 511. Game Play Analysis I */
select player_id, 
       min(event_date) as first_login
    from Activity
    group by player_id


/* 1179. Reformat Department Table */
select id,
       max(case when month='Jan'then revenue end) as Jan_Revenue,
       max(case when month='Feb'then revenue end) as Feb_Revenue,
       max(case when month='Mar'then revenue end) as Mar_Revenue,
       max(case when month='Apr'then revenue end) as Apr_Revenue,
       max(case when month='May'then revenue end) as May_Revenue,
       max(case when month='Jun'then revenue end) as Jun_Revenue,
       max(case when month='Jul'then revenue end) as Jul_Revenue,
       max(case when month='Aug'then revenue end) as Aug_Revenue,
       max(case when month='Sep'then revenue end) as Sep_Revenue,
       max(case when month='Oct'then revenue end) as Oct_Revenue,
       max(case when month='Nov'then revenue end) as Nov_Revenue,
       max(case when month='Dec'then revenue end) as Dec_Revenue
       from Department
       group by id;


/* 1173. Immediate Food Delivery I */
select round(
        count(case when order_date=customer_pref_delivery_date then 1 else null end)
        /count(*)*100,2) as immediate_percentage
    from Delivery
    

/* 595. Big Countries */
select name,
       population,
       area
    from World
    where area>3000000 or population>25000000;


/* 613. Shortest Distance in a Line */
select min(abs(p1.x-p2.x)) as shortest
    from point p1
    join point p2
    on p1.x!= p2.x


/* 1148. Article Views I */
select distinct author_id as id
    from Views
    where author_id = viewer_id
    order by author_id


/* 1327. List the Products Ordered in a Period */
select product_name,
       sum(unit) as unit
    from Products p
    left outer join
    (select * from Orders
        where order_date between "2020-02-01" and "2020-02-29") o 
    on p.product_id = o.product_id
    group by product_name
    having sum(unit)>=100

/* 1050. Actors and Directors Who Cooperated At Least Three Times */
select actor_id,
       director_id
    from ActorDirector
    group by actor_id, director_id
    having count(*)>=3


/* 586. Customer Placing the Largest Number of Orders */
select customer_number
    from orders
    group by customer_number
    order by count(*) desc
    limit 1


/* 584. Find Customer Referee */
select name
    from customer
    where referee_id!=2 or referee_id is Null


/* 1280. Students and Examinations */
select stdt.student_id,
       stdt.student_name,
       sub.subject_name,
       coalesce(exm.attended_exams,0) as attended_exams
    from students stdt
    cross join Subjects sub
    left outer join 
        (select student_id, 
                subject_name, 
                count(*) as attended_exams
            from Examinations
            group by student_id, subject_name) exm
    on stdt.student_id = exm.student_id 
    and sub.subject_name = exm.subject_name
    order by stdt.student_id, sub.subject_name


/* 1241. Number of Comments per Post */
select p.sub_id as post_id,
       coalesce(number_of_comments, 0 ) as number_of_comments
from
(select sub_id
    from Submissions
    where parent_id is Null
    group by sub_id
 ) p
 left outer join
 (select parent_id, 
         count(distinct sub_id) as number_of_comments
    from Submissions
    where parent_id is not Null
    group by parent_id) c
on p.sub_id = c.parent_id


/* 1211. Queries Quality and Percentage */
select query_name, 
       round(sum(rating/position)/count(rating), 2) as quality,
       round(count(case when rating<3 then 1 else null end)/count(rating)*100, 2) as poor_query_percentage
    from Queries
    group by query_name


/* 620. Not Boring Movies */
select * from cinema 
where id%2=1 and description !='boring'
order by rating desc;


/* 577. Employee Bonus */
select name,
       bonus
    from Employee e
    left outer join Bonus b
    on e.empId = b.empId
    where bonus is Null or bonus<1000


/* 1075. Project Employees I */
select project_id, 
       round(sum(experience_years)/count(project_id),2) as average_years
    from Project p
    left outer join Employee e
    on p.employee_id = e.employee_id
    group by project_id


/* 610. Triangle Judgement */
select x,y,z,
       case when (x+y>z and y+z>x and x+z>y) then 'Yes' 
       else 'No' end as triangle
    from triangle


/* 1294. Weather Type in Each Country */
select country_name,
       weather_type
    from 
    (select country_id,
            case when sum(weather_state)/count(weather_state)<=15 then "Cold" 
            when sum(weather_state)/count(weather_state)>=25 then "Hot"
            else "Warm" end as weather_type 
        from Weather
        where day between "2019-11-01" and "2019-11-30"
        group by country_id) w
    left outer join Countries c
    on c.country_id = w.country_id


/* 1113. Reported Posts */
select extra as report_reason,
       count(distinct post_id) as report_count
    from Actions
    where action='report'
    and action_date = "2019-07-04"
    group by extra


/* 603. Consecutive Available Seats */
select c.seat_id 
    from cinema c
    left outer join cinema n
    on c.seat_id+1 = n.seat_id
    left outer join cinema p
    on c.seat_id-1 = p.seat_id
    where c.free=1 and 
            (n.free=1 or 
                ((n.free is null and p.free=1) or 
                 (n.free=0 and p.free=1)))

select distinct a.seat_id
    from cinema a, cinema b
    where abs(b.seat_id - a.seat_id) =1 and
        a.free = 1 and b.free =1
    order by a.seat_id;


/* 607. Sales Person */
select name
    from salesperson
    where sales_id not in 
        (select distinct sales_id
            from orders o
            join company c
            on o.com_id = c.com_id
            where c.name='RED')


/* 182. Duplicate Emails */
select Email from Person
group by Email
having count(*)>=2;


/* 175. Combine Two Tables */
select FirstName,
       LastName,
       City,
       State
    from Person p
    left outer join Address a
    on p.PersonId = a.PersonId;


/* 1322. Ads Performance */
select ad_id, 
       case when sum(click)+sum(viewed)=0 then 0.00
       else round(sum(click)/(sum(click)+sum(viewed))*100,2)
       end as ctr
    from
    (select ad_id,
       case when action='Clicked' then 1 else 0 end as click,
       case when action='Viewed' then 1 else 0 end as viewed
    from Ads)u
    group by ad_id
    order by ctr desc, ad_id asc


/* 1084. Sales Analysis III */
select s.product_id,
       p.product_name
    from 
    (select product_id, 
        case when sale_date between "2019-01-01" and "2019-03-31" then 0
        else 1 end as month_order
        from Sales) s
    left outer join Product p
    on s.product_id = p.product_id
    group by s.product_id
    having max(month_order)=0


/* 512. Game Play Analysis II */
 select a.player_id,
       device_id
    from Activity a
    join 
    (select player_id,
            min(event_date) as min_event_date
        from Activity
        group by player_id)e
    on a.player_id=e.player_id and a.event_date = e.min_event_date   

Select player_id,
       device_id 
    from
    (select player_id, min(event_date), device_id
        from Activity 
        group by player_id) as a


/* 181. Employees Earning More Than Their Managers */
select e.Name as Employee
    from Employee e
    left outer join Employee m
    on e.ManagerId = m.Id
    where e.Salary > m.Salary;


/* 1141. User Activity for the Past 30 Days I */
select activity_date as day, 
      count(distinct user_id) as active_users 
    from activity
    group by day
    having abs(datediff(day,'2019-07-27'))<30  



/* 1076. Project Employees II */
select project_id
    from Project
    group by project_id
    having count(distinct employee_id) = 
    (select max(emp_counts) 
        from 
        (select project_id, 
                count(distinct employee_id) as emp_counts
            from Project
            group by project_id
        ) e 
    )



/* 1083. Sales Analysis II */
select buyer_id 
    from 
    (select s.buyer_id,
            sum(case when product_name='S8' then 1 else 0 end) as product_1,
            sum(case when product_name='iPhone' then 1 else 0 end) as product_3
        from 
        (select * from Sales) s
         left outer join Product p
         on s.product_id = p.product_id
        group by s.buyer_id
     ) pp
     where pp.product_1>=1 and pp.product_3=0

SELECT buyer_id
    from Sales s
    JOIN Product p
    ON p.product_id = s.product_id
    GROUP BY s.buyer_id
    HAVING AVG(product_name = 'S8') 
    AND NOT AVG(product_name = 'iPhone');


/* 183. Customers Who Never Order */
select Name as Customers
    from Customers c
    left outer join Orders o
    on c.Id = o.CustomerId
    where o.Id is Null


/* 619. Biggest Single Number */
select max(num) as num
    from 
    (select num
        from my_numbers
        group by num
        having count(*)=1) u


/* 596. Classes More Than 5 Students */
select class from courses
group by class
having count(distinct student)>=5


/* 197. Rising Temperature */
select c.Id
    from Weather c
    left outer join Weather p
    on DATEDIFF(c.RecordDate, p.RecordDate)=1
    where c.Temperature>p.Temperature


/* 176. Second Highest Salary */
select max(Salary) as SecondHighestSalary
from Employee
where Salary!= (select max(Salary) from Employee)

select (
    select distinct Salary 
        from Employee
        order by Salary desc
        limit 1 offset 1) as SecondHighestSalary;


/* 1393. Capital Gain/Loss */
select stock_name,
        sum(case when operation='Sell' then price
            else price*(-1) end) as capital_gain_loss
    from Stocks
    group by stock_name


/* 1270. All People Report to the Given Manager */
select e1.employee_id 
    from Employees e1
    left outer join Employees e2
    on e1.manager_id = e2.employee_id
    left outer join Employees e3
    on e2.manager_id = e3.employee_id
    where e1.employee_id!=1 and e3.manager_id=1


/* 1398. Customers Who Bought Products A and B but Not C */
select c.customer_id,
       customer_name
    from Orders o
    left outer join 
    Customers c
    on o.customer_id = c.customer_id
    group by c.customer_id,customer_name
    having (sum(product_name='A')>=1 
                and sum(product_name='B')>=1
                and sum(product_name='C')=0)


/* 1077. Project Employees III */
select p.project_id, p.employee_id
    from Project p
    left outer join Employee e
    on p.employee_id = e.employee_id
    inner join 
    (select p.project_id, 
           max(e.experience_years) as max_experience_years
        from Project p
        left outer join Employee e
        on p.employee_id = e.employee_id
        group by p.project_id) m
    on p.project_id = m.project_id and e.experience_years = m.max_experience_years


select t.project_id, t.employee_id
    from 
        (select p1.project_id, 
                p1.employee_id, 
                DENSE_RANK() OVER (PARTITION BY p1.project_id ORDER BY e1.experience_years DESC) AS r
            from Project p1 
            join Employee e1 
            on p1.employee_id = e1.employee_id
    ) as t
where t.r = 1


/* 1126. Active Businesses */
select e.business_id       
    from Events e
    left outer join 
    (select event_type, avg(occurences) as avg_occurences
        from Events
        group by event_type
     ) o
     on e.event_type = o.event_type
     group by e.business_id
     having sum(case when e.occurences>o.avg_occurences then 1 else 0 end)>1

select business_id 
    from events e 
    join
        (select event_type
                ,avg(occurences) as avg_occ 
            from events 
            group by event_type) t
    on e.event_type=t.event_type and e.occurences>t.avg_occ
    group by business_id 
    having count(*)>1
/* 1355. Activity Participants */
select activity
    from Friends
    group by activity
    having count(id) not in     
    (select max(counts)
        from(
            select activity, count(id) as counts
            from Friends
            group by activity
            )u
     union all
     select min(counts)
        from(
            select activity, count(id) as counts
            from Friends
            group by activity
            )u
    )

with temp as 
(select activity, count(distinct id)as num)
    from friends
    group by activity)
select temp.activity
    from temp
    where temp.num!=(select max(num) from temp)
    and temp.num!=(select min(num) from temp)

select name as activity
    from (select a.name, 
                rank() over(order by count(f.id) desc) rank1,
                rank() over(order by count(f.id) ) rank2
                from activities a
                left join friends f
                on a.name=f.activity
                group by a.name) tp
    where rank1!=1 and rank2!=1


/* 570. Managers with at Least 5 Direct Reports */
select m.Name as Name
    from Employee m
    left outer join Employee e
    on m.Id = e.ManagerId
    group by m.Name
    having count(e.Name)>=5



/* 1341. Movie Rating */
select * from 
(select u.name as results
    from
    (select user_id, 
            count(rating) as movie_counts
        from Movie_Rating
        group by user_id
    )m
    left outer join Users u
    on m.user_id = u.user_id
    order by movie_counts desc, u.name asc
    limit 1
 ) u1
 
 union all
 
 select * from (
 select m1.title
    from 
    (select movie_id,
            avg(rating) as avg_rating
        from Movie_Rating
        where created_at between '2020-02-01' and '2020-02-29'
        group by movie_id
    )r
    left outer join Movies m1
    on r.movie_id = m1.movie_id
    order by avg_rating desc, m1.title asc
    limit 1
 ) u2




/* 626. Exchange Seats */


/* 1158. Market Analysis I */
select user_id as buyer_id,
       join_date,
       count(o.buyer_id) as orders_in_2019
    from Users u
    left outer join 
    (select * from Orders 
        where order_date between "2019-01-01" and "2019-12-31")o
    on u.user_id = o.buyer_id
    group by user_id,join_date


/* 1070. Product Sales Analysis III */
select s.product_id,
       s.year as first_year,
       s.quantity,
       s.price
    from Sales s
    join 
    (select product_id, min(year) as first_year
        from Sales
        group by product_id) y
    on s.product_id = y.product_id and s.year=y.first_year


/* 184. Department Highest Salary */
# Write your MySQL query statement below
select m.Department as Department,
       e.Name as Employee,
       e.Salary as Salary
    from 
    (select d.Id,
           d.Name as Department,
           max(Salary) as max_sal
        from Employee e
        left outer join Department d
        on e.DepartmentId = d.Id
        group by d.Id, d.Name) m
    join
    Employee e
    on m.Id = e.DepartmentId and m.max_sal = e.Salary

select d.Name as Department, 
       e.Name as Employee, 
       e.Salary as Salary
    from Employee e
    join Department d
    on e.DepartmentId = d.Id
    where (e.DepartmentId, e.Salary) in
        (select  DepartmentId, 
                 max(Salary) as maxsalary 
            from Employee group by 1)