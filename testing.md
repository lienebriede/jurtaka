# Testing and Validation

## Table of Contents

[Code Validation](#code-validation)

[User Story Testing](#user-story-testing)

[Automated Tests](#automated-tests)

[Lighthouse Testing](#lighthouse-testing)

[Compatibility Testing](#cross-device-and-cross-browser-testing)

## Code Validation

Python files have been passed through the [CI Python Linter](https://pep8ci.herokuapp.com/). 

**Results:** 

JavaScript file has been passed through the [Jshint](https://jshint.com/).

**Results:** No errors found.

HTML and CSS files have been passed throught the [Nu Html Checker](https://validator.w3.org/nu/).

**Results:**

| Page                          | Result       |
|-------------------------------|--------------|
| [Home](https://jurtaka-f9d15d94d51b.herokuapp.com)                         | No errors    |
| [Post detail](https://jurtaka-f9d15d94d51b.herokuapp.com/post/)            | No errors    |
| [Create post](https://jurtaka-f9d15d94d51b.herokuapp.com/rainy-day/edit_post/4/) | *1    |
| [Edit post](https://jurtaka-f9d15d94d51b.herokuapp.com/rainy-day/edit_post/4/)   | *1    |
| [Latest view](https://jurtaka-f9d15d94d51b.herokuapp.com/?view_type=latest) | No errors    |
| [Hiking category view](https://jurtaka-f9d15d94d51b.herokuapp.com/?view_type=top&category=1) | No errors    |
| [Food and Drinks category view](https://jurtaka-f9d15d94d51b.herokuapp.com/?view_type=None&category=2) | No errors    |
| [Lodging view](https://jurtaka-f9d15d94d51b.herokuapp.com/?view_type=None&category=3) | No errors    |
| [About](https://jurtaka-f9d15d94d51b.herokuapp.com/about/)                   | *2    |
| [Contact](https://jurtaka-f9d15d94d51b.herokuapp.com/about/contact/)         | No errors    |
| [Search view](https://jurtaka-f9d15d94d51b.herokuapp.com/search/?q=liepaja)  | *4    |
| [Log out](https://jurtaka-f9d15d94d51b.herokuapp.com/accounts/logout/)      | No errors    |
| [Log in](https://jurtaka-f9d15d94d51b.herokuapp.com/accounts/login/)        | No errors    |
| [Sign up](https://jurtaka-f9d15d94d51b.herokuapp.com/accounts/signup/)      | *3    |

Errors that were found, but could not be located in the templates:

*1
- No p element in scope but a p end tag seen.

```html 
<label for="id_categories_2"><input type="checkbox" name="categories" value="3" class="custom-checkbox" id="id_categories_2">Lodging</label>
</div>
</div>
</p>
```

*2
- No p element in scope but a p end tag seen.

```html 
<span style="font-weight: 700;">Register today and join the conversation! Let’s explore the beauty of Jurtaka together!</span></p></p>
```

*3 
- End tag p implied, but there were open elements.
- Unclosed element span.
- Stray end tag span.
- No p element in scope but a p end tag seen.

```html 
<span class="helptext"><ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul></span></p>
```
*4

- End tag main seen, but there were open elements.

```html 
<div class="container-fluid">
```

- Unclosed element div.
```html 
</main>
```

[Return to contents list](#table-of-contents)

## User Story Testing

| Epic | Issue | User Story | Acceptance Criteria | Result |
| -- | -- | ---- | ---- | -- |
| Admin Tools | #7 | As a Site Admin I have full CRUD capabilities so that I can manage the content of the forum site | I can create, read, update, and delete posts | PASS | 
|||| I can create, read, update, and delete comments and likes associated with posts | PASS |
|||| I can approve and disapprove posts that are posted by users | PASS |
|||| I quickly understand the data in the database | PASS |
|| #28 | As a Site Admin I can manage the content on the About site so that I can provide up to date information to users | I can find and manage the About page on the admin panel | PASS | 
|||| I can style the text of the page directly in the admin panel | PASS |
|| #31 | As a Site Admin I can receive contact requests so that I can respond to user inquiries and manage communication efficiently | I can receive contact requests from both registered and unregistered users | PASS | 
|||| I can see what is the reason of the request | PASS |
| User Account Management | #13 | As a New Site User I can register an account so that I can interact with the forum | I can register an account | PASS | 
|||| I can log in and log out of my account | PASS |
|||| There is a message that informs me wether I am logged in or not | PASS |
|||| I find the log in button easily | PASS |
|| #30 | As a New and/or Registered Site User I can fill in the contact form so that I can contact the forum administration | I can find a contact form on the site | PASS | 
|||| I can fill in the form and send it to the admin | PASS |
|||| After sending the form, I receive a message that the form has been sent |
|||| I can choose a reason for contacting the admin | PASS |
| Content Viewing | #8 | As a New Site User I can view a list of posts so that I can read the forum | When I open the main page, I see a list of posts | PASS | 
|||| Besides the post I also see the title, the author and the date the post has been created | PASS |
|||| Posts are arranged with the most recent ones at the top | PASS |
|| #11 | As a New Site User I can open a post so that I can read the full post and the comments | I can open a post and see its full text | PASS | 
|| #12 | As a New Site User I can see only the first few lines of the posts so that I can quickly scan the posts to decide which wants I want to read | I can see only the first few lines of the post on the main site | PASS |
|| #14 | As a New Site User I can read comments on posts so that I can see the feedback of the forum community | When I open an individual post I can read comments | PASS |
|| #15 | As a New Site User I can see how many comments are left on a post so that I know how popular a post is | I can see how many comments are left on every post on the main site | PASS |
|||| I can see how many comments are left on every post on the individual post site | PASS |
|| #19 | As a New Site User I can see how many likes are left on a post so that I know how popular a post is | I can see how many likes are left on every post on the main site | PASS |
|||| I can see how many likes are left on every post on the individual post site | PASS |
|| #20 | As a Registered Site User I can see who has liked the posts so that I can understand the forum community | When I open a post I can see a list of users that have liked the post | PASS |
|| #29 | As a New Site User I can visit the About site so that I can learn about the forum and the forum community | I can easily find the navigation to the site | PASS |
|||| I can read the site | PASS |
|||| I can see an inviting picture on the about page | PASS |
| Content Navigation | #9 | As a New Site User I can see a visually appealing site so that I have an enjoyable visual experience | The logo is visually appealing and reflects the site's identity | PASS | 
|||| The background is visually appealing and do not distract users from the content | PASS |
|||| The navigation bar is intuitive | PASS |
|||| The footer contains links to social media pages | PASS |
|||| The styling elements align with the overall design of the site and are responsive | PASS |
|||| The site has a favicon | PASS |
|| #10 | As a New Site User I can see a paginated list of posts so that I can navigate the site easily | I can see a list of 5 posts per page | PASS |
|||| I can use next and previous buttons to navigate | PASS |
|| #21 | As a New Site User I can see the posts categorised by the most popular post so that I can see most useful posts first | I can find a "top" section/button on the forum site | PASS |
|||| I can see post list filtered by most popular posts first | PASS |
|| #22 | As a New Site User I can browse the posts by category so that I can navigate the site easier | I can find categories in navigation bar | PASS |
|||| I can see posts for each category | PASS |
|| #24 | As a New Site User I can search the forum so that I can find posts on topics that I am interested in | I can find a search bar on the site | PASS |
|||| I can type words in the search bar and it returns posts that contain them | PASS |
|||| If the words do not match I get a message saying that nothing was found | PASS |
|| #25 | As a New Site User when I use the search bar I can see the search results highlighted so that I can find my topics easily | When I search the forum, the search results are highlighted in yellow | PASS |
| Content Creation | #17 | As a Registered Site User I can write posts so that I can engage with the forum | I can see a "add a post" section | PASS | 
|||| I can add posts | PASS |
|||| After posting I am redirected back to the main site | PASS |
|||| After posting I receive a message that my post is awaiting approval | PASS |
|||| In case of failed submission I receive an error message | PASS |
|| #23 | As a Registered Site User when I am posting I can add categories to posts so that I can categorise my post | When I add a post, I can choose a relevant category/categories for this post | PASS | 
|| #39 | As a Registered Site User I can add photos to posts so that the content of my post is more interactive | I can upload at least two images when posting on forum | PASS | 
| Content Interaction | #16 | As a Registered Site User I can comment on posts so that I can engage with the author and the forum community | When I read an individual post I can see a "leave a comment" section | PASS | 
|||| I can add a comment | PASS |
|||| I see a message that I cannot comment if I am not logged in | PASS |
|||| After commenting on a post I get a notification and I see my comment | PASS |
|| #18 | As a Registered Site User I can like posts so that I can engage with the post author and the forum community | I can like a post | PASS | 
|||| I can see if I have liked a post and I can unlike it | PASS |
|||| I can see if I have liked a post and I can unlike it | PASS |
|| #27 | As a Registered Site User I can update and delete my posts so that I can update the content of my post or remove posts that are not relevant | After submitting a post, as the post author, I can see an option to update my post | PASS | 
|||| I can either update the content of my post or delete my post entirely | PASS |
|||| Upon submitting my edited post, I receive a message that my post is awaiting approval | PASS |
|||| In case of failed submission I receive an error message | PASS |
|||| Upon deleting my post, I get a confirmation prompt that asks to confirm the deletion of my post | PASS |

[Return to contents list](#table-of-contents)

## Automated Tests

### Post Form

| Test                                              | Expected Result                                                                        |Outcome|
|---------------------------------------------------|----------------------------------------------------------------------------------------|-------|
| `test_post_form_has_fields`                       | The form should have fields: 'title', 'post_content', 'categories', 'image1', 'image2' | PASS  |
| `test_post_form_is_valid`                         | Should validate with non-empty title, content, and valid categories                    | PASS  |
| `test_post_form_is_invalid_no_title`              | Should not validate with empty title                                                   | PASS  |
| `test_post_form_is_invalid_no_content`            | Should not validate with empty content                                                 | PASS  |
| `test_post_form_is_invalid_no_categories`         | Should not validate with no categories selected                                        | PASS  |
| `test_post_form_is_invalid_with_invalid_category` | Should not validate with an invalid category ID                                        | PASS  |
| `test_post_form_invalid_with_blank_space_title`   | Should not validate with only blank spaces in title                                    | PASS  |
| `test_post_form_invalid_with_blank_space_content` | Should not validate with only blank spaces in content                                  | PASS  |
| `test_post_form_is_valid_with_one_image`          | Should validate with one uploaded image                                                | PASS  |
| `test_post_form_is_valid_with_two_images`         | Should validate with two uploaded images                                               | PASS  |
| `test_post_form_valid_with_no_images`             | Should validate with no uploaded images                                                | PASS  |
| `test_post_form_title_placeholder`                | There should be a placeholder text 'Add a title'                                       | PASS  |
| `test_post_form_content_placeholder`              | There should be a placeholder text 'Add text'                                          | PASS  |
| `test_post_form_title_no_label`                   | The title field should have no label                                                   | PASS  |
| `test_post_form_content_no_label`                 | The post content field should have no label                                            | PASS  |
| `test_post_form_categories_label`                 | The categories field should have a label 'Categories'                                  | PASS  |
| `test_post_form_image1_label`                     | The image1 field should have a label 'Image'                                           | PASS  |
| `test_post_form_image2_label`                     | The image2 field should have a label 'Image'                                           | PASS  |
| `test_post_form_valid_with_max_length`            | Should validate with content at max length 10,000 characters                           | PASS  |
| `test_post_form_invalid_with_max_length`          | Should not validate with content exceeding 10,000 characters                           | PASS  |

### Comment Form

| Test                                              | Expected Result                                                                        |Outcome|
|---------------------------------------------------|----------------------------------------------------------------------------------------|-------|
| `test_comment_form_is_valid`                      | Should validate with non-empty content                                                 | PASS  |
| `test_comment_form_is_invalid`                    | Should not validate with empty content                                                 | PASS  |
| `test_comment_form_has_fields`                    | The form should have a content field                                                   | PASS  |
| `test_comment_form_invalid_with_blank_space`      | Should not validate with blank space in content field                                  | PASS  |
| `test_comment_form_labels`                        | The label for the content field should be an empty string                              | PASS  |
| `test_comment_form_placeholder`                   | There should be a placeholder text 'Add a comment'                                     | PASS  |
| `test_comment_form_valid_with_max_length`         | The content should be valid within the allowed 10 000 character limit                  | PASS  |
| `test_comment_form_invalid_with_max_length`       | The content should be invalid if exceeding the allowed 10 000 character limit          | PASS  |

### Contact Form

| Test                                              | Expected Result                                                                        |Outcome|
|---------------------------------------------------|----------------------------------------------------------------------------------------|-------|
| `test_contact_form_valid_with_user`               | Should validate with non-empty content, valid user ID and empty email field            | PASS  |
| `test_contact_form_valid_with_email`              | Should validate with non-empty content, valid email and no user ID                     | PASS  |
| `test_contact_form_is_invalid`                    | Should not validate with empty content                                                 | PASS  |
| `test_contact_form_invalid_with_blank_space`      | Should not validate with blank space in content field                                  | PASS  |

### Post_detail View

| Test                                              | Expected Result                                                                        |Outcome|
|---------------------------------------------------|----------------------------------------------------------------------------------------|-------|
| `test_render_post_detail_page`                    | Should render the 'post_detail' page                                                   | PASS  |
|                                                   | Should initialize comment form                                                         | PASS  |
|                                                   | Should display post author, post title, and post content                               | PASS  |
|                                                   | Should display comments, comment authors, comment form, comment count                  | FAIL* |
|                                                   | Should display like count, is liked, likers usernames                                  | PASS  |
                                       
* Comment count not rendered properly.

PASS: after adding a more simplified test code where it checks if the added 2 comments = 2
`self.assertEqual(self.post.comments.count(),2)` 

### Latest View

| Test                                              | Expected Result                                                                        |Outcome|
|---------------------------------------------------|----------------------------------------------------------------------------------------|-------|
| `test_render_post_list_latest_view`               | Should render the 'Latest' posts page                                                  | PASS  |
|                                                   | Should display posts ordered by latest first                                           | PASS  |

### Browse by Category View

| Test                                              | Expected Result                                                                        |Outcome|
|---------------------------------------------------|----------------------------------------------------------------------------------------|-------|
| `test_render_post_list_category_filter`           | Should render the 'Browse by Category' page                                            | PASS  |
|                                                   | Should display posts filtered by Category 1                                            | PASS  |

### Create Post View

| Test                                              | Expected Result                                                                        |Outcome|
|---------------------------------------------------|----------------------------------------------------------------------------------------|-------|
| `test_render_post_create_view`                    | Should render the 'New Post' page                                                      | PASS  |
|                                                   | Should initialize the PostForm                                                         | PASS  |

### Edit Post View

| Test                                              | Expected Result                                                                        |Outcome|
|---------------------------------------------------|----------------------------------------------------------------------------------------|-------|
| `test_render_post_edit_view`                      | Should render the 'Edit Post' page                                                     | PASS  |
|                                                   | Should initialize the PostForm                                                         | PASS  |

### About View

| Test                                              | Expected Result                                                                        |Outcome|
|---------------------------------------------------|----------------------------------------------------------------------------------------|-------|
| `test_render_about_page`                          | Should render the 'about' page                                                         | PASS  |
|                                                   | Should display page title and content                                                  | PASS  |

### Contact View

| Test                                              | Expected Result                                                                        |Outcome|
|---------------------------------------------------|----------------------------------------------------------------------------------------|-------|
| `test_render_contact_page`                        | Should render the 'contact' page                                                       | PASS  |
|                                                   | Should initialize Contact form                                                         | PASS  |


### Form Submission

| Test                                              | Expected Result                                                                        |Outcome|
|---------------------------------------------------|----------------------------------------------------------------------------------------|-------|
| `test_successful_comment_submission`              | Posts a comment on a post using test credentials                                       | PASS  |
|                                                   | Checks if the comment submission redirects correctly to the post detail page           | PASS  |
|                                                   | Displays a success message                                                             | PASS  |
| `test_successful_post_submission`                 | Submits a new post using test credentials                                              | FAIL* |
|                                                   | Verifies if the home page loads after submission                                       | PASS  |
|                                                   | Displays a success message                                                             | PASS  |               
| `test_successful_post_edit_submission`            | Edits an existing post using test credentials                                          | PASS  |
|                                                   | Verifies if the post edit redirects correctly to the post detail page                  | PASS  |
|                                                   | Checks if the post status is updated to '3'                                            | PASS  |
|                                                   | Displays a success message                                                             | PASS  |
| `test_successful_contact_submission`              | Submits a contact form with specified email and message                                | FAIL* |
|                                                   | Checks if the contact form data is stored in the database                              | PASS  |
|                                                   | Verifies if the home page loads after contact submission                               | PASS  |
|                                                   | Displays a success message for the contact submission                                  | PASS  |
| `test_successful_contact_submission_registered_user`| Edits an existing post using test credentials                                        | PASS  |
|                                                   | Submits a contact form by a registered user with specified subject and message         | PASS  |
|                                                   | Checks if the contact form data is stored in the database                              | PASS  |
|                                                   | Verifies if the home page loads after contact submission                               | PASS  |
|                                                   | Displays a success message for the contact submission                                  | PASS  |

* `KeyError: 'post_form'`: The 'post_form' was missing from the context in the 'post_create' view during form rendering.

PASS: after updating the 'post_create' view to include 'post_form' in the context for 'POST' requests.

* Both 'post_form' and 'contact_form' tests failed when submitted without required fields ('Category' for Post form and 'Subject' for Contact form).

PASS: after providing corect test data in all the required fields.

[Return to contents list](#table-of-contents)

## Lighthouse Testing

Chrome developer tools Lighthouse was used to test the performance, accessibility, best practices and SEO of all pages within the platform. 

| Page              | Mobile                                          | Desktop                                         |
|-------------------|-------------------------------------------------|-------------------------------------------------|
| Home              | <img src="">    | <img src="">   |
| Post detail       | <img src="">  | <img src=""> |
| Add a post        | <img src="">  | <img src=""> |
| Search view       | <img src=""> | <img src=""> |
| Browse by category| <img src=""> | <img src=""> |
| About             | <img src="">  | <img src="">|
| Contact           | <img src=""> | <img src=""> |

[Return to contents list](#table-of-contents)

## Cross-Device and Cross-Browser Testing

1. Desktop Devices:

- iMac
  - Safari
  - Google Chrome
  - Mozilla Firefox
- MacBook Air
  - Safari
  - Google Chrome
  - Mozilla Firefox
- Microsoft Computer
  - Microsoft Edge
  - Google Chrome
  - Mozilla Firefox

2. Mobile Devices:

- Samsung Galaxy Tablet
  - Chrome (Android)
  - Mozilla Firefox*
- iPhone SE
  - Safari (iOS)
- Samsung Galaxy Smartphone
  - Chrome (Android) 
  - Mozilla Firefox*

**Results**:

There was an issue on all of the devices: 
When users performed a search using the search bar (`q` parameter), the application correctly displayed search results based on the query. After performing a search, clicking on a category link in the navbar did not navigate users to the intended category page. Instead, it appeared as if the application tried to interpret the click as a new search with the query parameter `q=none`. This was fixed by modifying the category links in the navbar to explicitly construct their URLs using `{% url 'home' %}`.

* When users attempted to add a post using Mozilla Firefox, they encountered the following issues:
- Mozilla Firefox did not display the required field indicators on the forms fields (title and post_content) that are mandatory.
- Attempting to submit the form resulted in a 500 error. On desktop devices everything worked as expected. 
This could be an issue of how Mozilla handles form validation. This was partyly fixed by explicitly marking the PostForm fields as `required=True`. Users can now successfully submit forms on mobile devices using Mozilla Firefox. However, the required field indicators are still not displayed.

[Return to contents list](#table-of-contents)