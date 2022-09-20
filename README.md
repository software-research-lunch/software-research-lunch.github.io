# Stanford Software Research Lunch Website

This is the repository for software-research-lunch.stanford.edu.  The template is based on https://github.com/poole/poole.

To test the site locally, run `make serve` (requires jekyll).

## How to prepare for a new quarter

1. Create a new entry in `_data/schedule.yml` for the new quarter.
2. Update `index.html` to use the new quarter's data.
3. Update `org.html` to use the new quarter's data.
4. Update `calendar.ics` to use the new quarter's data.
5. Create the file `archive/YEAR-QUARTER.html` (and fill it based on one of the other templates).
6. Add a link to the now past quarter in `_includes/main.html` under "Past quarters".  If you had a upcoming quarter listed as "Future quarter", remove that.
7. Make sure that the domain does not need to be renewed.  See https://vanityurl.stanford.edu/.


## When to hold talks

So far, the rule has been: Every week of the quarter, including end-of-quarter period, but not during finals week or breaks.  Not during the summer quarter.

## Managing the Stanford subdomain

Anjiang Wei owns software-research-lunch.stanford.edu and it can be changed via https://vanityurl.stanford.edu/. The website is automatically published via Github Pages here: https://software-research-lunch.github.io/

## Email to Non-Stanford Speakers

Hi,

Could you please send me a title, abstract and a short bio for the announcement?

Some information on the Stanford Software Research Lunch:  It starts at noon with a catered lunch, and the talk then starts at 12:15pm and goes until 1pm (including questions and discussion).  This is usually a hard deadline, as some people will have to leave, but interested people can stay longer for an offline discussion.  The lunch is in Gates 415, on the 4th floor of the Computer Science building (353 Serra Mall, Stanford).

The audience consists of mostly graduate students from Stanford interested in programming languages research as well as faculty from this area.  The talk is open to all though, so there may also be one or two other interested people.

If you plan on driving, Andrea Villanueva (CC'ed here) can help you with parking information and reimbursing parking fees.

If you have any trouble finding us, feel free to email me or call at xxx-xxx-xxxx.


## TODO when handing organization over to somebody else

1. Give them access to the github repository.
2. Transfer the domain here https://tools.stanford.edu/cgi-bin/vhost-request.
3. Change all occurrences of OLD-ORGANIZER to NEW-ORGANIZER in this repository.  Right now these are in `_includes/main.html`, `_includes/program.html`.
4. Change all occurrences of OLD-ORGANIZER-PHONE to NEW-ORGANIZER-PHONE.  Right now this is only in the file `README.md`
5. Give them admin access to `software-research-lunch@lists.stanford.edu` by going to https://mailman.stanford.edu/mailman/listinfo/software-research-lunch.

