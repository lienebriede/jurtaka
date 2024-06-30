# Testing and Validation

## Contents

[User Story Testing](#user-story-testing)

[Test Cases](#form-testing)


## User Story Testing

| Epic | Issue | User Story | Acceptance Criteria | Result |
| -- | -- | ---- | ---- | -- |
| Admin Tools | #7 | As a Site Admin I have full CRUD capabilities so that I can manage the content of the forum site | I can create, read, update, and delete posts | To be checked | 
|||| I can create, read, update, and delete comments and likes associated with posts | To be checked |
|||| I can approve and disapprove posts that are posted by users | To be checked |
|||| I quickly understand the data in the database | To be checked |
|| #28 | As a Site Admin I can manage the content on the About site so that I can provide up to date information to users | I can find and manage the About page on the admin panel | To be checked | 
|||| I can style the text of the page directly in the admin panel | To be checked |
|| #31 | As a Site Admin I can receive contact requests so that I can respond to user inquiries and manage communication efficiently | I can receive contact requests from both registered and unregistered users | To be checked | 
|||| I can see what is the reason of the request | To be checked |
| User Account Management | #13 | As a New Site User I can register an account so that I can interact with the forum | I can register an account | To be checked | 
|||| I can log in and log out of my account | To be checked |
|||| There is a message that informs me wether I am logged in or not | To be checked |
|||| I find the log in button easily | To be checked |
|| #30 | As a New and/or Registered Site User I can fill in the contact form so that I can contact the forum administration | I can find a contact form on the site | To be checked | 
|||| I can fill in the form and send it to the admin | To be checked |
|||| After sending the form, I receive a message that the form has been sent |
|||| I can choose a reason for contacting the admin | To be checked |
| User Account Management | #8 | As a New Site User I can view a list of posts so that I can read the forum | When I open the main page, I see a list of posts | To be checked | 
|||| Besides the post I also see the title, the author and the date the post has been created | To be checked |
|||| Posts are arranged with the most recent ones at the top | To be checked |
|| #11 | As a New Site User I can open a post so that I can read the full post and the comments | I can open a post and see its full text | To be checked | 
|||| I can exit the post and return to the post list | To be checked |
|| #12 | As a New Site User I can see only the first few lines of the posts so that I can quickly scan the posts to decide which wants I want to read | I can see only the first few lines of the post on the main site | To be checked |
|| #14 | As a New Site User I can read comments on posts so that I can see the feedback of the forum community | When I open an individual post I can read comments | To be checked |
|| #15 | As a New Site User I can see how many comments are left on a post so that I know how popular a post is | I can see how many comments are left on every post on the main site | To be checked |
|||| I can see how many comments are left on every post on the individual post site | To be checked |
|| #19 | As a New Site User I can see how many likes are left on a post so that I know how popular a post is | I can see how many likes are left on every post on the main site | To be checked |
|||| I can see how many likes are left on every post on the individual post site | To be checked |
|| #20 | As a Registered Site User I can see who has liked the posts so that I can understand the forum community | When I open a post I can see a list of users that have liked the post | To be checked |
|| #29 | As a New Site User I can visit the About site so that I can learn about the forum and the forum community | I can easily find the navigation to the site | To be checked |
|||| I can read the site | To be checked |
|||| I can see an inviting picture on the about page | To be checked |
| Content Navigation | #9 | As a New Site User I can see a visually appealing site so that I have an enjoyable visual experience | The logo is visually appealing and reflects the site's identity | To be checked | 
|||| The background is visually appealing and do not distract users from the content | To be checked |
|||| The navigation bar is intuitive | To be checked |
|||| The footer contains links to social media pages | To be checked |
|||| The styling elements align with the overall design of the site and are responsive | To be checked |
|||| The site has a favicon | To be checked |
|| #10 | As a New Site User I can see a paginated list of posts so that I can navigate the site easily | I can see a list of 5 posts per page | To be checked |
|||| I can use next and previous buttons to navigate | To be checked |
|| #21 | As a New Site User I can see the posts categorised by the most popular post so that I can see most useful posts first | I can find a "top" section/button on the forum site | To be checked |
|||| I can see post list filtered by most popular posts first | To be checked |
|| #22 | As a New Site User I can browse the posts by category so that I can navigate the site easier | I can find categories in navigation bar | To be checked |
|||| I can see posts for each category | To be checked |
|| #24 | As a New Site User I can search the forum so that I can find posts on topics that I am interested in | I can find a search bar on the site | To be checked |
|||| I can type words in the search bar and it returns posts that contain them | To be checked |
|||| If the words do not match I get a message saying that nothing was found | To be checked |
|| #25 | As a New Site User when I use the search bar I can see the search results highlighted so that I can find my topics easily | When I search the forum, the search results are highlighted in yellow | To be checked |
| Content Creation | #17 | As a Registered Site User I can write posts so that I can engage with the forum | I can see a "add a post" section | To be checked | 
|||| I can add posts | To be checked |
|||| After posting I am redirected back to the main site | To be checked |
|||| After posting I receive a message that my post is awaiting approval | To be checked |
|| #23 | As a Registered Site User when I am posting I can add categories to posts so that I can categorise my post | When I add a post, I can choose a relevant category/categories for this post | To be checked | 
|| #39 | As a Registered Site User I can add photos to posts so that the content of my post is more interactive | I can upload at least two images when posting on forum | To be checked | 
| Content Interaction | #16 | As a Registered Site User I can comment on posts so that I can engage with the author and the forum community | When I read an individual post I can see a "leave a comment" section | To be checked | 
|||| I can add a comment | To be checked |
|||| I see a message that I cannot comment if I am not logged in | To be checked |
|||| After commenting on a post I get a notification and I see my comment | To be checked |
|| #18 | As a Registered Site User I can like posts so that I can engage with the post author and the forum community | I can like a post | To be checked | 
|||| I can see if I have liked a post and I can unlike it | To be checked |
|||| I can see if I have liked a post and I can unlike it | To be checked |
|| #27 | As a Registered Site User I can update and delete my posts so that I can update the content of my post or remove posts that are not relevant | After submitting a post, as the post author, I can see an option to update my post | To be checked | 
|||| I can either update the content of my post or delete my post entirely | To be checked |
|||| Upon deleting my post, I get a confirmation prompt that asks to confirm the deletion of my post | To be checked |

## Form Testing

| Form          | Test                                         | Expected Result                                                               | Outcome |
|---------------|----------------------------------------------|-------------------------------------------------------------------------------|---------|
| Comment Form  | `test_comment_form_is_valid`                 | Should validate with non-empty content                                        | PASS    |
|               | `test_comment_form_is_invalid`               | Should not validate with empty content                                        | PASS    |
|               | `test_comment_form_has_fields`               | The form should have a content field                                          | PASS    |
|               | `test_comment_form_invalid_with_blank_space` | Should not validate with blank space in content field                         | PASS    |
|               | `test_comment_form_labels`                   | The label for the content field should be an empty string                     | PASS    |
|               | `test_comment_form_placeholder`              | There should be a placeholder text 'Add a comment'                            | PASS    |
|               | `test_comment_form_valid_with_max_length`    | The content should be valid within the allowed 10 000 character limit         | PASS    |
|               | `test_comment_form_invalid_with_max_length`  | The content should be invalid if exceeding the allowed 10 000 character limit | PASS    |
|---------------|----------------------------------------------|-------------------------------------------------------------------------------|---------|
| Contact Form  | `test_contact_form_valid_with_user`          | Should validate with non-empty content, valid user ID and empty email field   | PASS    |
|               | `test_contact_form_valid_with_email`         | Should validate with non-empty content, valid email and no user ID            | PASS    |
|               | `test_contact_form_is_invalid`               | Should not validate with empty content                                        | PASS    |
|               | `test_contact_form_invalid_with_blank_space` | Should not validate with blank space in content field                         | PASS    |
|---------------|----------------------------------------------|-------------------------------------------------------------------------------|---------|


## View Testing




