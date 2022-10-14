# combine-multiple-flask-projects

* project1 and project2 contains 2 simple projects with js, templates and routes('/','/test')
* Then projects are combined by adding url_prefix as '/project1', '/project2'

## Advantages:
This Project provides the ability to 
1. combine multiple client-based same product
2. host them in the same project 
3. reside scripts(.py,.js,.css,.html) with same name with contradicting each other

## Disadvantages:
1. Takes too much time to restart the server
2. If one project fails to restart due to changes, other projects become unavailable