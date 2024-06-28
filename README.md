# Jurtaka Hiking Forum

- Table of Contents
## User Experience

### User Stories

As a **Site Admin** I can create, read, update and delete data so that I can manage the content of the forum site [issue #7](https://github.com/lienebriede/jurtaka/issues/7) 

As a **New Site User** I can view a list of posts so that I can read the forum [issue #8](https://github.com/lienebriede/jurtaka/issues/8)

As a **New Site User** I can see a visually appealing site so that I have an enjoyable visual experience [issue #9](https://github.com/lienebriede/jurtaka/issues/9)

As a **New Site User** I can see a paginated list of posts so that I can navigate the site easily [issue #10](https://github.com/lienebriede/jurtaka/issues/10)

As a **New Site User** I can open a post so that I can read the full post and the comments [issue #11](https://github.com/lienebriede/jurtaka/issues/11)

As a **New Site User** I can see only the first few lines of the posts so that I can quickly scan the posts to decide which wants I want to read [issue #12](https://github.com/lienebriede/jurtaka/issues/12)

As a **New Site User** I can register an account so that I can interact with the forum [issue #13](https://github.com/lienebriede/jurtaka/issues/13)

As a **New Site User** I can read comments on posts so that I can see the feedback of the forum community [issue #14](https://github.com/lienebriede/jurtaka/issues/14)

As a **New Site User** I can see how many comments are left on a post so that I know how popular a post is [issue #15](https://github.com/lienebriede/jurtaka/issues/15)

As a **Registered Site User** I can comment on posts so that I can engage with the author and the forum community [issue #16](https://github.com/lienebriede/jurtaka/issues/16)

As a **Registered Site User** I can write posts so that I can engage with the forum [issue #17](https://github.com/lienebriede/jurtaka/issues/17)

As a **Registered Site User** I can like posts so that I can engage with the post author and the forum community [issue #18](https://github.com/lienebriede/jurtaka/issues/18)

As a **New Site User** I can see how many likes are left on a post so that I know how popular a post is [issue #19](https://github.com/lienebriede/jurtaka/issues/19)

As a **Registered Site User** I can see who has liked the posts so that I can understand the forum community [issue #20](https://github.com/lienebriede/jurtaka/issues/20)

As a **New Site User** I can see the posts categorised by the most popular post so that I can see most useful posts first [issue #21](https://github.com/lienebriede/jurtaka/issues/21)

As a **New Site User** I can browse the posts by category so that I can navigate the site easier [issue #22](https://github.com/lienebriede/jurtaka/issues/22)

As a **Registered Site User** when I am posting I can add categories to posts so that I can categorise my post [issue #23](https://github.com/lienebriede/jurtaka/issues/23)

As a **New Site User** I can search the forum so that I can find posts on topics that I am interested in [issue #24](https://github.com/lienebriede/jurtaka/issues/24)

As a **New Site User** when I use the search bar I can see the search results highlighted so that I can find my topics easily [issue #25](https://github.com/lienebriede/jurtaka/issues/25)

As a **Registered Site User** I can edit and delete my comment so that I can update content of my comment or remove comments that are not relevant [issue #26](https://github.com/lienebriede/jurtaka/issues/26)

As a **Registered Site User** I can update and delete my posts so that I can update the content of my post or remove posts that are not relevant [issue #27](https://github.com/lienebriede/jurtaka/issues/27)

As a **Site Admin** I can manage the content on the About site so that I can provide up to date information to users [issue #28](https://github.com/lienebriede/jurtaka/issues/28)

As a **New Site User** I can visit the About site so that I can learn about the forum and the forum community [issue #29](https://github.com/lienebriede/jurtaka/issues/29)

As a **New Site User/Registered Site User** I can fill in the contact form so that I can contact the forum administration [issue #30](https://github.com/lienebriede/jurtaka/issues/30)

As a **Site Admin** I can receive contact requests so that I can respond to user inquiries and manage communication efficiently [issue #31](https://github.com/lienebriede/jurtaka/issues/31)

As a **Registered Site User** I can add photos to posts so that the content of my post is more interactive [issue #39](https://github.com/lienebriede/jurtaka/issues/39)



#### Changes

- Update and delete my posts [issue #27](https://github.com/lienebriede/jurtaka/issues/27)

This user story required more story points than initially estimated. Story points were increased from 4 to 6.

- Edit and delete my comment [issue #26](https://github.com/lienebriede/jurtaka/issues/26)

The user story needed revision because the approach of adding and editing comments resulted in poor user experience. The layout of the post detail page makes editing comments in the planned manner difficult for the users, as the "add comment" field is located just below the post, while the published comment that needs editing could be at the bottom of the page. To avoid confusion, comments should be edited directly within the published comment field. This change, however, requires more story points for this user story.

## Site Structure
    
### Site maps

This site map shows the intended structure of the site. The grey colored boxes relate to the 'could have' user stories or future implementations at the stage of planning.

![Site Map](/documentation/sitemap_jurtaka.png)


### Database schemas

This ERD shows the intended database structure. The blue colored tables (HikeSection and HikeRating) relate to the 'could have' user stories or future implementations at the stage of planning.

![ERD](/documentation/db_schema_jurtaka.png)

## Database Schema Enhancements

Some changes were implemented to the database schemas. 

- The "Post" model has been implemented with a field **'has_been_edited'** Boolean field to differentiate between original and edited posts. This addition enables to display the "updated_on" date only for posts that have been edited.  

- The "Contact" model has been implemented with an **'email'** field to make it possible for unregistered users to provide their contact information. Setting 'null=True, blank=True' allows this field to be optional, allowing both registered and unregistered users to submit the form. 

- The **'reason'** field has been removed from the "Contact" model. Since the contact form already includes a **'subject'** field, having two separate fields for subject and reason is redundant for submitting contact inquiries.

- Both the "Post" and "About" models have been implemented with  Cloudinary **'image'** fields. This allows admins to upload an image for the "About" page and the users to add one or two images to their posts.
 	
# Agile Methodology:

![Kanban board](/documentation/kanban_screenshot.png)


  MoSCoW Prioritisation
-	Features
  Future features
-	Technologies used
-	Validation and testing

## Bugs and Fixes

1. NoReverseMatch Error on Post Approval

After adding a post, users encountered a "NoReverseMatch" error.

**Reason:** There is a unique slug required for each post to generate a correct URL for approved posts. Since users do not provide slugs when adding posts, the system cannot match requested URLs with post details and this leads to an error.

**Fix:** The bug was fixed by implementing an automatic slug generator using the 'slugify' library in Django models:

```from django.utils.text import slugify```

and adding a method that generates a slug automatically:

```python
def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super().save(*args, **kwargs)
```

This overrides the 'save' method in the model. First, it checks if a slug already exists, if not, it generates one.  In this way the title is converted to a slug and each post has a unique identifier in its URL.

2. 404 Error on post_detail View for Posts Awaiting Approval

When an edited post was submitted, the post_detail view could not retrieve the post, causing a 404 error. 

**Reason:** When a post is edited, its status is set to "update pending" (status=3). The bug was caused because the post_detail view was retrieving only posts with the "approved" status (status=1). The edited post with its status set to "update pending" was not available to the post_detail view, resulting in a "Page not found" error.

**Fix:** The bug was fixed by adjusting the post_detail view to include both statuses:

```queryset = Post.objects.filter(slug=slug, status__in=[1, 3])```

This makes it possible for users to view details of their edited posts while awaiting admin approval. Also in this way the original slug is used in the redirection, avoiding conflicts related to URLs.

3. Comment Count Issue on Search Results Page

Comments were not counted on the search results page.

**Reason:** Comments were not being counted on the search results page due to the way Django manages relations between the Post, Comment and Like models using foreign keys. On the post_list page counts were accessed using ```post.comments.count()``` and ```post.likes.count()```
However, on search_results page Django did not automatically count comments for each post. 

**Fix:** This was fixed by importing 'Q' class from django.db.models and adding ```annotate(comment_count=Count('comments'))``` to the queryset in the search_results view. This annotation instructs Django to calculate and include the comment count for each post.

4. UX Confusion with 'Back' Button

Initially, the individual post page featured a 'Back' button intended to enhance user navigation. Users could view individual posts either from the main home page or from the search results. The 'Back' button was designed to bring them back to the home page or the search results, respectively. This was accomplished by adding the ```HTTP_REFERER``` header to the post_detail view and setting the referer variable in the post_detail template. The ```HTTP_REFERER``` header indicates the URL of the page from which the user navigated, ensuring that the 'Back' button would bring users back to their previous page, thus enhancing the user experience.

However, the implementation of this feature led to unintended user experience issues. When users submitted comments or edited their posts, the 'Back' button did not function as expected. Instead of returning users to their previous page, it often resulted in confusion, as the 'Back' button would not work. 

To avoid this confusion the 'Back' button was removed from the post_detail template. The remaining buttons are:
'Exit' button on account related templates and 'Back' button on the post_create template.

5. Comment Count Not Updating After Adding Comment

The code did not update the comment_count variable after saving a new comment. 

**Reason:** Even though a new comment was added succesfully, the count displayed in the template ```{{ comment_count }}``` remained the same until the page was refreshed. This happened because the variable was not recalculated and rendered in the template.

**Fix:** This was fixed by adding changes to post_detail view:
```comment_count = post.comments.count()``` was added after saving a new comment. This insures that the comment count reflexts the current number of comments after a new comment is added. 
The view was adjusted with ```return redirect('post_detail', slug=slug)``` This ensures that the page is updated with the new comment count without requiring a manual refresh.

6. Conflict in Form Submissions for Like/Unlike and Comment

When users liked or unliked a post, a "required field" message appeared under the comment form.

**Reason:** Both the 'like' and 'comment' forms were submitting to the same post_detail URL. This caused confusion because the server expected data from both forms simultaneously, and this lead to the error. 

**Fix:** This was fixed by adding a separate 'like_post' URL for handling likes. A hidden input field was added to the form, which now captures the current URL, allowing the server to redirect users back to the original post detail page after processing the like action. This separation of handling likes and comments prevents conflicts between the submissions.

-	Deployment
-	Credits

