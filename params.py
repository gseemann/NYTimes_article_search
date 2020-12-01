######### UPDATE file with variables to use while running test.py script (defaults provided) ##############

## COLUMN NAMES for df that stores all the info
##NOTE: Program will ignore unexpected column names. Be sure this list is inclusive of all the info you care to store
col_names = ['_id',
             'abstract',
             'byline.organization',
             'byline.original',
             'byline.person',
             'document_type',
             'headline.content_kicker',
             'headline.kicker',
             'headline.main',
             'headline.name',
             'headline.print_headline',
             'headline.seo',
             'headline.sub',
             'keywords',
             'lead_paragraph',
             'multimedia',
             'news_desk',
             'print_page',
             'print_section',
             'pub_date',
             'section_name',
             'snippet',
             'source',
             'subsection_name',
             'type_of_material',
             'uri',
             'web_url',
             'slideshow_credits',
             'word_count']

##What to search NYT Article Finder for
search = 'Silicon Valley'

##How many batches to run(note each batch returns 10 articles)
batch = 10
offset = 0

##Output df file location
file_out = 'output/output_df.csv'





