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

As a **Registered Site User** I can edit and delete my comment so that I can update content of my comment or remove comments that are not relevant [issue #26](https://github.com/lienebriede/jurtaka/issues/26)

As a **Registered Site User** I can update and delete my posts so that I can update the content of my post or remove posts that are not relevant [issue #27](https://github.com/lienebriede/jurtaka/issues/27)



## Site Structure
    
### Site maps

This site map shows the intended structure of the site. The grey colored boxes relate to the 'could have' user stories or future implementations at the stage of planning.

![Site Map](/documentation/sitemap_jurtaka.png)


### Database schemas

This ERD shows the intended database structure. The blue colored tables (HikeSection and HikeRating) relate to the 'could have' user stories or future implementations at the stage of planning.

![ERD](/documentation/db_schema_jurtaka.png)

## Database Schema Enhancements

Some changes were implemented to the database schemas. 
The "Post" model has been implemented with a field **'has_been_edited'** Boolean field to differentiate between original and edited posts. This addition enables to display the "updated_on" date only for posts that have been edited.  
 	
-	Agile Methodology:

![Kanban board](/documentation/kanban_screenshot.png)


  MoSCoW Prioritisation
-	Features
  Future features
-	Technologies used
-	Validation and testing

## Bugs and Fixes

### NoReverseMatch Error on Post Approval

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

### 404 Error on post_detail View for Posts Awaiting Approval

When an edited post was submitted, the post_detail view could not retrieve the post, causing a 404 error. 

**Reason:** When a post is edited, its status is set to "update pending" (status=3). The bug was caused because the post_detail view was retrieving only posts with the "approved" status (status=1). The edited post with its status set to "update pending" was not available to the post_detail view, resulting in a "Page not found" error.

**Fix:** The bug was fixed by adjusting the post_detail view to include both statuses:

```queryset = Post.objects.filter(slug=slug, status__in=[1, 3])```

This makes it possible for users to view details of their edited posts while awaiting admin approval. Also in this way the original slug is used in the redirection, avoiding conflicts related to URLs.

-	Deployment
-	Credits

