# Exploring Perspectives on the Impact of Artificial Intelligence on
# the Creativity of Knowledge Work: Beyond Mechanised
# Plagiarism and Stochastic Parrots
## Advait Sarkar
### Microsoft Research, University of Cambridge, University College London
### United Kingdom
### advait@microsoft.com
## ABSTRACT

Artificial Intelligence (AI), and in particular generative models,
are transformative tools for knowledge work. They problematise
notions of creativity, originality, plagiarism, the attribution of credit,
and copyright ownership. Critics of generative models emphasise
the reliance on large amounts of training data, and view the output
of these models as no more than randomised plagiarism, remix, or
collage of the source data. On these grounds many have argued for
stronger regulations on the deployment, use, and attribution of the
output of these models.
However, these issues are not new or unique to artificial intelli-
gence. In this position paper, using examples from literary criticism,
the history of art, and copyright law, I show how creativity and
originality resist definition as a notatable or information-theoretic
property of an object, and instead can be seen as the property of a
process, an author, or a viewer. Further alternative views hold that
all creative work is essentially reuse (mostly without attribution),
or that randomness itself can be creative. I suggest that creativity
is ultimately defined by communities of creators and receivers, and
the deemed sources of creativity in a workflow often depend on
which parts of the workflow can be automated.
Using examples from recent studies of AI in creative knowledge
work, I suggest that AI shifts knowledge work from material pro-
duction to critical integration. This position paper aims to begin a
conversation around a more nuanced approach to the problems of
creativity and credit assignment for generative models, one which
more fully recognises the importance of the creative and curatorial
voice of the users of these models, and moves away from simpler
notational or information-theoretic views.

## CCS CONCEPTS

- Human-centered computing→Interaction design theory,
concepts and paradigms;HCI theory, concepts and models;•
Computing methodologies→Artificial intelligence;Machine
learning;•Applied computing→Arts and humanities;•Social
and professional topics→Intellectual property.

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany
©2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0807-7/23/06... $15.
https://doi.org/10.1145/3596671.

## KEYWORDS

```
critical theory
ACM Reference Format:
Advait Sarkar. 2023. Exploring Perspectives on the Impact of Artificial Intelli-
gence on the Creativity of Knowledge Work: Beyond Mechanised Plagiarism
and Stochastic Parrots. InAnnual Symposium on Human-Computer Interac-
tion for Work 2023 (CHIWORK 2023), June 13–16, 2023, Oldenburg, Germany.
ACM, New York, NY, USA, 17 pages. https://doi.org/10.1145/3596671.
```
## 1 INTRODUCTION

```
In October 2022, creators using AI-generated art faced fierce op-
position, including death threats, from the manga community in
Japan [ 43 ], because the art strongly mimicked the styles of well-
known manga artists, clearly enabled by the use of copyrighted
illustrations in the training data. The Japanese anime and manga
industries have long been accepting of fan art that directly reuses
copyrighted work, and to some extent even encourages it, as it stim-
ulates engagement with the franchise. But using AI to generate this
artwork seemed to cross a line. It seemed to push beyond the limit
of cultural acceptability. Something about the nature of mechanical
production signals a shift in our relationship with creativity and
knowledge work.
To begin to unpick this shift, we need a clearer articulation of
creativity. This we can get from Margaret Boden [ 19 ], for whom
a creative idea is surprising, novel, and valuable.^1 An idea may
be novel with respect to the individual person (“P-creativity”) or
with respect to a historical community (“H-creativity”). It is either
the production of a novel (and surprising, and valuable) idea from
within a pre-defined conceptual space, or the transformation of
conceptual space to enable new forms of idea.
Blackwell develops this definition by observing that “surprise”
can be defined in information-theoretic terms [ 16 ]. The information
content of a message is a measure of how surprising it is; a message
that is not surprising at all provides no new information. More-
over, drawing on Dennett’s notion of the intentional stance [ 44 ],
Blackwell argues that even when AI produces something surprising,
novel, and valuable, it cannot be creative, because that would incor-
rectly assume that the model itself has beliefs, goals, and desires.
In other words, it cannot be creative because it is notintentional.
It would thus be incorrect to attribute creativity to the model, as
it would be incorrect to attribute the capacity for arithmetic to a
calculator [ 35 ]. Rather, any creativity in this instance arises from
the human activity of constructing a “performance” on the basis
```
(^1) Variations of this “three-criterion” definition for creativity are widely adopted, as for
example by the US Patent Office [124].


```
CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany Advait Sarkar
```
of this random output, as a Tarot card reader produces a creative
performance on the basis of a randomised arrangement of cards.
Moreover, Blackwell argues that the stochastic reuse of training
data, even when arranged into novel forms, is not a truly novel
idea; it is the execution and replay of human behaviour encoded
into these systems. It is a form of objectivity laundering [ 15 ], where
inherently subjective human judgements are replayed in an algo-
rithmically objectified manner. Yet these “stochastic parrots” [ 10 ],
as Gebru, Bender, et al. term them, cannot be extricated from the
subjective biases inherent in their training data. With this view of AI
as mechanical replay of subjective judgements, Sarkar argues that
the phrase “human-AI collaboration” ought to be avoided, because
it implies that AI is a creative collaborator, responsible for a certain
share of labour, rather than those who provided the training data,
who are the true collaborators in any human-AI “collaboration”
[119].
With these precepts in place, it is possible to assess the creativity
or plagiaristic nature of AI with respect to its training data and
with respect to the wider world of information content. When an
AI system repeats a sentence (or image, etc.) from its training data,
it is not creative because it does not fulfil the criterion for new
information, and it is a plagiarist because it can do so without
attribution. When it repeats an idea or ideology from its training
data, albeit in a unique and novel way, it is not creative because
that idea derives from behaviour exemplified in the training set,
and it may still be a plagiarist if it is the intellectual content of the
idea and not the words used to describe it (or image used to depict
it, etc.) that we consider to be original intellectual property [ 82 ].
And when it produces a genuinely novel, surprising, and valuable
idea, it may not be a plagiarist, but it cannot be considered creative
because to do so would be to take an intentional stance.
There is extensive commentary on the nature of computers and
creativity, far too much to include in this brief introduction (indeed
practically every paper published in the long-running ACM confer-
ence on Creativity & Cognition^2 is a candidate for inclusion). There
are relevant reviews of the field [ 4 , 18 , 52 , 138 ]. However I hope to
have captured the salient points germane to the discussion of the
current generation of artificial intelligence, primarily foundation
models and large language models. These have been articulated by
Boden, Blackwell, Bender, Dennett, Gebru, Sarkar, etc. as follows:
creativity is information-theoretic surprise, with authorial intent.
AI systems generate content through randomised reuse without
intent or attribution; they are therefore not creative and tend to
facilitate plagiarism. The danger is clear: integrating these systems
into everyday knowledge workflows (writing documents, creat-
ing graphics, etc.) is likely to lead to a collective loss of creativity,
an increase in mechanised plagiarism, and “undermining creative
economies” [140].
These are valid, important, and logical perspectives on creativity
and plagiarism. My aim in this paper is not to dismantle or refute
them. However, I am concerned that these perspectives only repre-
sent a small fraction of the plurality of perspectives on creativity
and plagiarism, all of which are equally valid, important, and logical.
In this paper, I will show with examples the following alternative
perspectives:

(^2) https://cc.acm.org/

- Process as creativity: that creativity lies not in the object of
    creation, but in the method of production (Section 2.1).
- Authorial intent and discourse as creativity: that the creative
    content of an object can only be understood with respect to
    the author’s intent, or the societal discourse surrounding it
    (Section 2.2).
- Interpretation as creativity: that creativity is not a property
    of an object but of the interaction between a reader and the
    object (Section 2.3).
- Reuse as creativity: that reuse of prior material without at-
    tribution is an unavoidable aspect of any creative endeavour
    (Section 2.4).
- Randomness as creativity: that random processes can be
    viewed as creative of their own accord, especially as a mech-
    anism to distance the (human) creator from the creation
    (Section 2.5).

```
After discussing these perspectives, I will explain how the form-
content distinction becomes a recurrent issue in creativity (Sec-
tion 3), and the challenges of relying on intellectual property law
to help understand whether AI is being creative (Section 4).
Each perspective raises several questions and harbours its own
contradictions and ethical shortcomings. Answering these ques-
tions and resolving these contradictions is impossible; it is precisely
the impossibility of this task that has given rise to such a plural-
ity of perspectives. However impossible, the exercise is not futile.
The result of considering these perspectives will be a new agenda
for understanding how creativity in knowledge work is affected
by AI, namely, as a shift from the direct production of knowledge
artefacts to thecritical integrationof AI output as part of a broader
knowledge workflow (Section 5).
To clarify the scope of this paper, it is worth briefly discussing
what is meant by AI, what is meant by knowledge work, and what
is the relationship between creativity and knowledge work. First,
“AI”. AI is a broad term that encompasses an unusually diverse,
heterogenous, and multidisciplinary set of concepts, stretching back
over two centuries [ 90 ]. When the term “AI” is used in this paper, it
is referring to contemporary, statistical, deep learning approaches
which use vast numbers of parameters and quantities of training
data to model a space of knowledge artefacts (e.g., images, texts) and
can be used to generate artefacts by sampling from this space. These
include foundation models [ 21 ], large language models [ 26 ], image
generation models [ 115 ], among others. These are often referred to
collectively as “generative AI”.
Next, “knowledge work”. This term was popularised by Peter
Drucker [ 46 ], for whom knowledge work was differentiated from
manual work by its focus on applying mental faculties and knowl-
edge acquired through systematic education. In this paper, I further
refine the scope of the term by adopting the key property identified
by Kidd [ 78 ], namely that knowledge work requires the private
transformation of the individual doing the work, as an outcome
of processing information. I further focus on those particular as-
pects of knowledge workflows that culminate in the production of
material artefacts such as documents, textual communication, im-
ages, presentations etc., upon which there is a cultural or corporate
```

```
The Impact of Artificial Intelligence on the Creativity of Knowledge Work CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany
```
expectation of creativity (as per Boden’s criteria). These production-
oriented tasks are directly affected by the AI technologies under
discussion.
Finally, how does creativity relate to knowledge work? In some
sense, the need for creativity in knowledge work falls out implicitly
from the joint definitions of Boden and Kidd: in order to be usefully
transformed by information processing, a knowledge worker must
synthesize a novel idea. This process of synthesis is depicted by
Wallas’ multi-stage model of creativity [ 137 ]. Not all aspects of
all knowledge work might be considered creative, and a notion of
creativity may rather be dependent on individual and group norms,
as Xu et al. argue [ 145 ]. In this paper, rather than attempt to draw
examples from the academic discourse on creativity in knowledge
work, we will look at the discourse on creativity in literature, music,
and art (among other fields). These are forms of knowledge work
in which the concerns around creativity are acutely and deeply
rooted, and consequently the discussion of creativity is particularly
rich and nuanced. Each section will conclude with a reflection on
how this discussion relates to the issues of AI and creativity in
knowledge work more broadly.

## 2 ALTERNATIVE CONCEPTIONS OF

## CREATIVITY

The current discourse around AI creativity and plagiarism focuses
on the information content of its output. In particular, its output is
measured and qualified in terms of familiar units of information:
tokens, words, bits, or pixels. This information content is considered
the primary or only determinant of the creativity of the output.
However, there are alternative views of creativity which de-
emphasise, or even ignore, the actual content of any objects pro-
duced as part of a creative process. These views move away from
contentand towardscontext. Sometimes, it is the process itself
which is considered creative, and the resultant objects are inciden-
tal. Sometimes, an object can be viewed as creative or un-creative
depending on the authorial intent and the social discourse which
accompanies it, or the way in which it is interpreted by the viewer.
Creativity may not be defeated by reuse, but entirely dependent on
it. Random processes may themselves be sources of creativity. This
section explains each of these views in turn.

## 2.1 Process as creativity

```
The artistic practice of conceptual art emphasises the process of
creating an artwork, and de-emphasises the resultant artefact [ 87 ].
In conceptual art, according to LeWitt,“all of the planning and deci-
sions are made beforehand and the execution is a perfunctory affair.
The idea becomes a machine that makes the art”. Conceptual artists
proceed by experimentation, sketching, and extensive prototyping,
until arriving at a method for executing or expressing an idea. This
method can be executed once, or many times, but it is itself the
true outcome of the creative process, not any particular execution.
Seeking a complete separation between process and outcome, some
practitioners proceeded“by making plans for their work and having
these plans executed by others [...] not simply by describing a desired
image, but by specifying the process by which the work was to be
made”[54].
```
```
The ideology of conceptual art was prefigured in abstract expres-
sionism, in particular “action painters” like Pollock and Gorky, who
emphasised the bodily motion and physicality of the art process
as essential to the content of the artwork. According to Froman
[ 53 ], action painting shifts“from painting where [...] the artist paints
toward the goal of an image [...] to painting where the artist comes to
the canvas as a site for acting, so that the painting displays the event
that takes place when the artist paints”. It was anticipated perhaps
earlier still in Brutalist architecture, which sought to expose and
exalt materials and construction processes, producing“structures
which were entirely visible, reducing historical ornament to a mini-
mum so that the exterior could reflect the inner structure rather than
hiding it”[34].
Conceptual art has a cognate practice in literature: conceptual
writing [ 1 ]. Conceptual writers proceed by writing with constraints
(deriving from the OuLiPo movement [ 73 ]), or under a set of gener-
ative rules. Many work with computer programs, or write programs
to facilitate the mechanised execution of writing rules (as in genera-
tive art [ 20 ]). The processes and rules are anterior to the generated
texts, and are considered the objects in which creativity resides.
Computing gives us a ready metaphor for this view. We are al-
ready accustomed to thinking of algorithms as distinct creative
contributions from any particular “run” of the algorithm with a cer-
tain input and output. Quicksort is a creative contribution distinct
from mergesort or bubblesort, despite the fact that every correct
sorting algorithm produces the same output as any other.
In a review of generative art practices, Boden and Edmonds point
out that it is difficult to pinpoint the “locus of creativity”, whether
it is in the individual artwork, or in the “art system” [ 20 ]. This is
not a question that can be logically answered from first principles,
but is continuously renegotiated by communities of art producers
and consumers. If in a particular context, creativity is viewed as a
property of the process and not the outcome, whether AI is being
creative or a plagiarist rests not on its output but rather whether its
algorithm, or the human-AI-data complex which comprises the cre-
ational “algorithm”, can be understood as distinct from or identical
to another.
```
## 2.2 Authorial intent and discourse as creativity

```
In 1917 Marcel Duchamp signed a porcelain urinal and submitted
it for an exhibition of the Society of Independent Artists. In doing
so, he is credited with creating the single most influential work of
modern art [ 67 ]. ThoughFountainwas not Duchamp’s first work
repurposing ordinary materials, and others such as Picasso were
experimenting with similar ideas at the time, its brazen statement
of counterculture brought a sharp and unprecedented clarity to the
underlying principle: Duchamp’s “readymades” contended that art,
and creativity, can come about from literally any object, through
the pure force of authorial intent. The more general term for this
kind of work is “found art”, both in the sense that it is art that can
be “found” in the environment, but also that it becomes art because
it is “found [to be] art” through discourse. Duchamp explained that
“an ordinary object [could be] elevated to the dignity of a work of art
by the mere choice of an artist”[81].
Duchamp’s urinal may seem far removed from our everyday ex-
perience of creative authorship. Yet as Goldsmith notes [ 1 ], the vast
```

CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany Advait Sarkar

majority of cultural transactions on the Internet revolve around
readymades:“To be the originator of something that becomes a
broader meme trumps being the originator of the actual trigger event
that is being reproduced. The “re-” gestures – such as reblogging and
retweeting – have become cultural rites of cachet in and of themselves.
If you can filter through the mass of information and pass it on as an
arbiter to others, you gain an enormous amount of cultural capital”. In
the era of social media, the curatorial intent behind re-sharing has
come to carry its own cultural cachet of creativity. Such is the role
of the “trail blazer” in Bush’s world of the Memex [ 28 ],“who find
delight in the task of establishing useful trails through the enormous
mass of the common record”.
Authorial intent can do more than directly imbue an object with
the property of being “creative”. Often, the author’s context and
stated intent are used to disambiguate vocabulary and references,
and to identify and interpret metaphors. Consider the following
lines from Maya Angelou’sCaged Bird[5]:

```
The free bird thinks of another breeze
and the trade winds soft through the sighing trees
and the fat worms waiting on a dawn bright lawn
and he names the sky his own.
```
```
But a caged bird stands on the grave of dreams
his shadow shouts on a nightmare scream
his wings are clipped and his feet are tied
so he opens his throat to sing.
```
Had Angelou been a well-known animal rights activist, the com-
mon interpretation of this poem would have been as an agitation
against keeping birds in cages. But she was, of course, a civil rights
activist, and with this knowledge one is justified in the interpreta-
tion that the birds are people, and the cage is racism. Works of art
and literature generally do not include biographies of the authors
and descriptions of their intent within the body of the work. It is
context from outside the content of the work which is nevertheless
essential for understanding the information content of the work,
and evaluating it as creative or otherwise. Borges’ delightful short
storyPierre Menard, Author of the Quixote[22] takes this idea to a
logical extreme, in which the author Menard has written (though
not copied) text identical to chapters from Cervantes’Don Quixote,
but which the narrator views as far superior due to differences
in historical circumstance between Menard and Cervantes:“The
Cervantes text and the Menard text are verbally identical, but the
second is almost infinitely richer. [...] It is a revelation to compare the
Don Quixote of Pierre Menard with that of Miguel de Cervantes”.
As Foucault notes, access to as-yet unpublished notes or new
information about an author, or even a return to familiar texts, can
affect and revise our interpretation of works and their meaning
[ 51 ]. A notable example of this is the publication in the late 1920s
and early 1930s of Marx’sEconomic and Philosophic Manuscripts
of 1844, which nearly a century after their writing finally enabled
a clearer interpretation of key concepts in Marxian philosophy,
such as “alienation”, which was poorly understood in Marx’s own
lifetime [102].
Creative objects exist not as individual quanta of information,
but in a reactive and shifting network. In this view, the meaning of
an AI-generated text and therefore its status as creative, is not static,

```
but may change depending on other texts that the AI generates,
and other discourse that we draw upon as interpretive resources
that support the text.
At this point, one might ask: to what extent is authorial intent
relevant to AI? We do not want to attribute undue personhood
or agency to the AI system itself (Dennett’s intentional stance).
Perhaps it is easier to argue that the human-AI-data complex re-
sponsible for a particular AI output is the author. However, it is
also possible to argue that AI itself can be considered an author,
without granting it personhood or agency.
Foucault considers the question of what an author entity, or
“author function” actually is [ 51 ], especially when used as an inter-
pretive resource to help establish the meaning of a text:“Modern
criticism, in its desire to ‘recover’ the author from a work [... is] remi-
niscent of Christian exegesis [... in determining the authors of a text
when it is unclear who wrote it.] According to Saint Jerome, there are
four criteria: the texts that must be eliminated from the list of works
attributed to a single author are those inferior to the others (thus, the
author is defined as a standard level of quality); those whose ideas
conflict with the doctrine expressed in the others (here the author is
defined as a certain field of conceptual or theoretical coherence); those
written in a different style and containing words and phrases not
ordinarily found in the other works (the author is seen as a stylistic
uniformity); and those referring to events or historical figures subse-
quent to the death of the author (the author is thus a definite historical
figure in which a series of events converge)”.
These criteria: a level of quality, conceptual coherence, stylistic
uniformity, and historicity, can be applied to AI to give it an author
function without also granting it agency or personhood. These
ways of producing an author entity may seem imprecise in our
modern world, where it is far easier to definitively establish the
author of a text, and often possible to ask them directly: “did you
write this?” and “what did you mean by this?” Even with these
powers, unavailable to Saint Jerome, we still conceive of authors in
Jeromian terms. For instance, Wittgenstein’s later work contrasts
so heavily with his earlier work that references often qualify him
as “early Wittgenstein” or “late Wittgenstein”, as though they were
two separate people (this is also sometimes done with Marx to
distinguish “young Marx” [ 103 ], presumably from “old Marx” but
the latter is rarely used). Artists’ lives are commonly periodised (e.g.,
Picasso’s “blue period”). This schizophrenic segmentation shows
that we are willing to detach a singular person from the authorial
entity or entities they gave rise to over the course of their life.
Legal conceptions of authorship have similarly long been divorced
of personhood, where “investments of capital and administrative
organisation” can constitute authorship [13].
In January 2023, several academic publishers, such as the Science
family of journals, updated their editorial policies to ban the naming
of ChatGPT as author on papers, some going as far as to prohibit
the use of AI technologies to generate content for papers altogether
(though it is unclear how this can be enforced) [ 133 ]. Ostensibly,
the practice of naming ChatGPT as an author stems from a desire
to attribute its “participation” in the creative process. Yet this was
not a safe or acceptable solution. A reason cited by publishers
for this ban is that authors are accountable for the content in their
papers, and ChatGPT is not an entity that can be held accountable to
anything by anyone. Publishers also interpreted the use of ChatGPT
```

The Impact of Artificial Intelligence on the Creativity of Knowledge Work CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany

output in a paper, as the (human) co-authors plagiarising text from
ChatGPT, even it when named as an author [ 133 ]. Again, we witness
a community response to the challenge of selecting one imperfect
notion of authorship (and therefore creativity, or plagiarism) among
a number of imperfect notions. The inclusion of ChatGPT as an
author in this scenario was culturally unacceptable because of one
particular interpretation of the author function.
A final example of how discourse, intent, and context deter-
mine the creative content of an object comes from our very own
discipline of interaction design. In research-through-design, the
aim is to produce knowledge by designing artefacts. The objects
in isolation carry no knowledge content; the objects are simply
design, not research-through-design. In research-through-design,
the creative knowledge content of an artefact (which is judged by
the community standards of peer review) depends on the rigour of
the methods applied, and the associated discourse which elaborates
the knowledge content and situates it with respect to related work
[56, 148].
With the view that creativity comes from authorial intent and
discourse, when considering whether a particular episode of AI-
assisted production is creative or not, we must not look only at the
output itself. The output may be even be “found” or “readymade”
from the training data, without attribution. A discursive assessment
of creativity will consider, in what context is this output being used
or presented? What is the authorial intent? What discourse is it
facilitating? Who or what are we considering to be the author
entity?

## 2.3 Interpretation as creativity

The previous discussion of meaning as constructed depending on
context raises the question of who is doing the construction. This
leads us to another family of ideas relating to the role of the observer
(viewer, reader, consumer) of an object in determining its creative
content. McLuhan puts it bluntly [ 93 ]:“A work of art has no existence
or function apart from its effects on human observers.”
The emphasis on the reader or viewer arose in part as a reac-
tion to the status quo of literary and art criticism in the mid-20th
century, which focused so heavily on authorial intent and context,
bordering on deification of the author. Barthes in his seminalDeath
of the Authorhighlights the shortcomings of this view and offers
a solution [ 9 ]:“it is language which speaks, not the author [...] to
give a text an Author is to impose a limit [...] In the multiplicity of
writing, everything is to be disentangled [...] writing ceaselessly posits
meaning [...] but there is one place where this multiplicity is focused
and that place is the reader”.
Abstract expressionism aimed to elevate the process of produc-
tion over the outcome. This also highlighted the artist’s embodied
presence in the work: the splashes of paint on a canvas by Pol-
lock echo the swing of his arms. This elevated the artist above
the viewer, which was an undesirable outcome for the counter-
movement known as Minimalism. Artists such as Frank Stella and
Kenneth Noland (and cognates in music: Steve Reich, Philip Glass,
Brian Eno, etc.) sought to distance and even remove the hand of
the author, using repetitive patterns, and a minimality of means,
meaning, and structure, thus hoping to increase the involvement
of the recipient in the work of art [ 135 ]. According to Bernard [ 14 ]:

```
“minimal art is aimed in part at achieving an impersonal quality,
avoiding the depiction of personality that most minimalist artists felt
had become entirely too explicit [...] to remove the accompanying
interposition of artist’s personality between artwork and viewer”.
In literature the counter-movement against authorial intent be-
came known as “reader-response criticism” [ 71 ]. Among the most
vehement proponents were the American New Critics, who rejected
the notion of authorial intent outright. The entire meaning of a
text was in the text itself, and information from outside the text
including and especially the author’s intent, was irrelevant in inter-
pretation. Having finished writing a text, the author is equivalent
to any other reader, and has no special claim to understanding the
work due to being its author. To value the author’s intent above
the interpretation of other readers was to commit theintentional
fallacy[ 143 ], a literary foreshadowing of Dennett’s intentional
stance. The position of the New Critics is perhaps too extreme to
defend, and counterexamples, such as the excerpt from Angelou in
the previous section, clearly exhibit the need for extrinsic context
for interpretation [ 106 ]. The trap of assuming that the substantive
content of a work can be derived purely from its form is the very
same one we fall into when evaluating the creativity of AI based
on its output. The point of reader-response criticism, however, is
that even when extrinsic information is discounted, the same form
can reveal different contents, different responses, depending on
the reader’s individual interpretation. The view of creativity as
interpretation tells us that in order to evaluate whether something
produced by AI is creative or not, we must ask: according to which
interpretation of the output?
Yet elevating the reader and the importance of interpretation also
has its own critics. According to critics of reader-response, allowing
for “interpretation” to create content from form is a license to trans-
form any work into anything else. At the extreme, interpretation
renders meaningless the formal differences between texts; any text
can be interpreted as having the meaning of any other text. Thus
Sontag protests [ 131 ]:“Interpretation [...] presupposes a discrepancy
between the clear meaning of the text and the demands of (later)
readers [...] The interpreter, without actually erasing or rewriting the
text, is altering it [...] interpretation excavates, and as it excavates,
destroys; it digs ‘behind’ the text, to find a sub-text which is the true
one. [...] interpretation is the revenge of the intellect upon art”. While
expressed so poetically, the universalism of this position is as dif-
ficult to defend as that of the New Critics; Sontag appears not to
acknowledge the role her own formidable and vengeful intellect
plays in creating the “clear meaning of the text”.
Many of these contradictory viewpoints are visible in the author-
reader relations of J. K. Rowling, author of the Harry Potter series
of fiction novels. The Harry Potter community looked to Rowling’s
authorial intent as an interpretive resource. When Rowling “re-
vealed” that Albus Dumbledore, a main character, was gay (despite
there being no evidence of this in the text), the community was
eager to re-interpret the books with this lens [ 70 ]. This declaration
of authorial intent signalled Rowling as an ally of the LGBTQ+ com-
munity. However, when Rowling’s playThe Cursed Childbegan
performances, the community accused Rowling of “queerbaiting”
[ 92 ], which is to use the suggestion of homoromatic interest to ap-
peal to the LGBTQ+ audience, while being non-committal enough
to avoid being alienating to heteronormative society. For many in
```

```
CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany Advait Sarkar
```
the LGBTQ+ community, the value of Rowling’s authorial intent
has been further undermined by her criticism of trans individuals,
and her claims that trans-positive discourse is harmful to children,
that trans activism is misogynist, and that trans women are a threat
to “biological” women [ 47 ]. In response, queer communities are re-
claiming the texts from Rowling’s authorial intent, and re-queering
them through fan fiction and community engagement.
The tumultuous relationship between Rowling and her commu-
nity of readers shows that while literary critics are free to spill
as much ink as they like for or against the intentional fallacy, for
or against interpretation, the most forceful and consequential ar-
biter of the content of a work is the community that consumes
it. Examples such as Rowling’s echo in miniature the Protestant
Reformation, perhaps the greatest of all community movements to
reclaim interpretation from author-ity. The force of the community
will also significantly shape the reception of artwork, literature,
and any knowledge artefact produced with AI.

## 2.4 Reuse as creativity

Recall the common position taken when assessing AI creativity: pla-
giarism is reuse without attribution. Reuse is permitted in creative
works, but only with attribution: the taint of plagiarism negates any
claim to creativity. Creativity and plagiarism are mutually exclusive.
Thus one can only be creative either by avoiding reuse altogether,
or by attributing every source on which one draws, which makes
clear thenovelcreative component of a particular work. But are
these tenets universally applicable?
This section describes an alternative conception of creativity
which holds that there is no such thing as creativity without reuse,
and that exhaustive attribution is literally impossible. Moreover,
norms around what constitutes “proper” attribution are not uni-
versal. In several historical circumstances, proper attribution has
been deliberately avoided; there are practical and ethical reasons
for “improper” attribution.
In literature the reuse inherent in every work is articulated by
Barthes [ 9 ]:“a text is [...] a multi-dimensional space in which a
variety of writings, none of them original, blend and clash. The text is
a tissue of quotations drawn from the innumerable centres of culture.
[...] the writer can only imitate a gesture that is always anterior, never
original. His only power is to mix writings, to counter the ones with
the others, in such a way as never to rest on any one of them.”
Despite all text being a “tissue of quotations”, we can still recog-
nise new works as creative and novel. InThe Anxiety of Influence,
Bloom examines the early 19thcentury Romantics to develop a the-
ory for how novelty can emerge from reuse [ 17 ]. Bloom posits that
all poets suffer from the anxiety of being derivative of precursor
poets. However, Bloom observes that “strong” poets can respond
in one of six ways to precursor poets, to create an original poetic
vision despite the anxiety of influence. For example, a poet can offer
a completion, or antithesis, to an idea “started” by a precursor poet.
It is important to note that the kind of reuse Barthes and Bloom
talk about is fundamentally unattributable. It is a probabilistic,
subconscious mixing of “innumerable centres of culture”, of all
sense-impressions and memories. If we take the Barthes/Bloom
view of all work as fundamentally reuse, all authorship as funda-
mentally under influence, then pointing out the reuse nature of

```
AI is redundant. The important question is how the AI output has
responded to the training data it reuses, and whether it can be said
to have constructed an original vision, e.g. by Bloom’s criteria or
by some other.
Not only do writers inexorably reuse ideas from other writers,
but they also rely on the ideas of readers to help construct meaning.
This is different from the earlier point about the role of reader
interpretation. The theory of “cognitive capitalism” [ 99 ] holds that
any work depends on the “general intellect”, a term mentioned
in passing by Marx, which cognitive capitalists have expanded to
mean the vast sets of knowledge and experience that are shared by
members of a culture, and which artists draw upon. A comedian
telling a “knock-knock” joke about waiting in line at a supermarket
relies on the general intellect of a culture that is familiar with the
form of such a joke, and also with supermarkets. Similarly, any text,
artwork, or knowledge artefact draws on a basis of innumerable
cultural, linguistic, and semantic connections – most of which is not,
cannot be, and need not be, attributed. Barthes extends this reliance
on general intellect to the very words of the author’s vocabulary [ 9 ]:
“[Should the author] wish to express himself, he ought at least to know
that the inner ‘thing’ he thinks to ‘translate’ is itself only a ready-
formed dictionary, its words only explainable through other words,
and so on indefinitely”. In text, words are re-used resources, given
meaning only by the network of associations in the general intellect
of the reader (some semioticians may disagree, but a discussion of
this is out of scope).
Words are fundamentally unattributable, as are concepts such
as the knock-knock joke or the supermarket, nor do we wish to
attribute them. If every work stands on a towering edifice of reused
associations, we select only a miniscule fraction of these as worthy
of attribution, depending on the context; this cultural delimitation of
attribution reflects societal judgements of where “value” comes from
in a work. These societal judgements are not moral universals, but
are continually negotiated and renegotiated by different actors in
the “value chain” of a knowledge work, to further private interests.
Numerous art forms are based on reuse. Collage, decoupage, and
montage have been employed since the high middle ages. The art
form of erasures, as in Tom Phillips’ Humument [ 112 ], creates new
texts by selectively erasing old ones. Reuse, when apparent, invites
an automatic comparison between the original work and its reused
form: this effect is exploited by subvertising, détournement, and
“culture jamming” to make artistic or political statements by cor-
rupting and re-imagining public advertising and signage [ 42 ]. The
attributional culture around each of these art forms does not require
the authors of the source scraps of material to be attributed. No one
demands attribution for the authors and photographers whose work
appears in the magazine and newspaper clippings which constitute
the Dadaist collage of Hannah Höch, or the pop art photomon-
tage of Richard Hamilton. These exemplify a distinct contextual,
community-driven interpretation of creativity, plagiarism, and fair
attributive norms.
Jazz improvisation includes the practice of “quotation”: the in-
clusion of small, well-known melodic/harmonic motifs by other
composers [ 101 ]. It is an encouraged and celebrated aspect of the
art form, and functions as a way for the performer to demonstrate
their knowledge of jazz repertoire, for them to converse and engage
with other composers, and as a sign of respect and attribution to
```

```
The Impact of Artificial Intelligence on the Creativity of Knowledge Work CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany
```
the quoted composers. Similarly, sampling practices in hip-hop
[ 121 ], and the practices of lyrical reference in rap music serve to
create a dialogue between artists and also to acknowledge mutual
creative influences. Unlike the world of textual attributions, which
operates through names and bibliometric document identifiers, the
attributional natures of quotation, sampling, and lyrical reference
rely on the listener’s knowledge and attitude. When a knowledge-
able listener hears a quotation or a sample, it is heard not as an
unattributed plagiarist reuse, but as a self-contained unit of conver-
sation, reuse, and attribution. It is simultaneously a hat-tip to the
prior composers and a wink at the audience. As the rapper Pusha T
puts it so succinctly:“If you know, you know”. This merging of cita-
tion and use, of quoting and attribution, was intolerable to Foucault,
who nonetheless observed, and attempted to justify, that such merg-
ing was inevitable even in the highly formal attributional norms
of scientific writing [ 66 ]. Jazz quoting, hip-hop sampling, and rap
references exemplify yet another distinct contextual, community-
driven interpretation of how reuse relates to creativity, plagiarism,
and fair attributive norms. Unfortunately, as we will see later, these
norms come into violent conflict with the blunt instruments of
copyright law.
Brueghel the Younger, a skilled painter but widely considered to
be relatively unoriginal in comparison to his father, made a career
out of copying and replicating his father’s designs [ 38 ]. Yet he was
not a plagiarist: he did not present his own works as those of his
father, he often subtly adapted the design to suit his customer’s
tastes, and he was extremely commercially successful and well-
respected in his day [ 79 ]. Modern critics who have labelled him a
knockoff or copycat are therefore inappropriately applying modern
ideals around creativity and originality, modern notions of the
artistic value chain alien to the ateliers of 16thcentury Flemish
painters, as though they are spatiotemporal universals.
In several historical circumstances, attribution has been deliber-
ately avoided. Victorian women often published under masculine
pen-names (e.g., Mary Anne Evans took the pen name George
Eliot; the Brontë sisters and Louisa May Alcott also took masculine
names) to increase the commercial acceptability of their work, and
to avoid negative societal stereotypes attached to women writers.
J.K. Rowling published a detective series under the pseudonym
Robert Galbraith, to spare the series from the inevitable and unfair
comparison to Harry Potter. Other writers published controversial
or contentious ideas under pen names to avoid persecution or cen-
sorship (e.g., Voltaire – already a pen name – was known to deny
the authorship of his controversial writings, preferring to attribute
them to imaginary or sometimes real people). Eric Blair took the
name George Orwell when publishing his memoir of growing up
in poverty, to protect his family from embarrassment. Some men
take on women’s names when writing for an audience comprised
of primarily women, in some cases multiple authors collaborate
under a single pen name [ 129 ]. The point is that there are many
legitimate reasons for subverting “proper” attribution which have
no bearing on deemed creativity.
Another case where the assumed relationship between creativ-
ity, attribution, and plagiarism is challenged is in the forgery. The
18 thcentury poet Thomas Chatterton forged numerous poems in

```
a medieval style, attributed to a 15thcentury priest, which signifi-
cantly influenced English, French, and German literature. Similar
episodes of forgery include James MacPherson’s “Ossian” and Ed-
ward Williams’ “Iolo Morganwg” [ 36 ]. There are many examples
in the world of visual art, as well. Initially, these forgeries are con-
sidered creative on account of their content and their presumed
authorship. Later, when the forgery is exposed, the creativity associ-
ated with these works does not disappear but is transformed. Today
we celebrate the ingenuity of Chatterton and Williams, and appreci-
ate the creative effort and talent required to masterfully reproduce
the form of another artist, with the same conflicted fascination that
we watch the protagonist in Frank Abagnale Jr.’sCatch Me If You
Can. It is not without reason that they are called con-artists.
If we take the view that creativity is fundamentally reuse, we
must recognise that every sentence we write, artwork we create, etc.
is not only generated by the superposition of influences from innu-
merable prior works, but is also given meaning in the world only by
reference to other works. We live in an era of unprecedented media
availability and saturation, which McLuhan dubbed the “electric
implosion” [ 93 ]. Filmmaker Kirby Ferguson’s documentary series
Everything is a Remixrecovers Barthes and Bloom in the digital
age [ 50 ]. It is easier than ever to find influences in our media envi-
ronment, and more difficult than ever to avoid them. The anxiety
induced in the Romantics by the passive, poetic influencer pales
in comparison to the anxiety induced in modern society by the ac-
tive, propagandistic social media influencer.“You Are Not a Parrot”,
declaresNew Yorkmagazine, confidently summarising the view
of linguist Emily Bender [ 141 ], who strongly resists any analogies
between human language production and the “stochastic parrot”
nature of large language models. Perhaps this view is defensible
from a linguistic perspective, but it has been repeatedly repudiated
from a literary perspective, a discipline which is decidedly closer
to the questions of creativity and plagiarism.
It is impossible to determine every influence on our work and
attribute them, so we settle on a culturally constructed compromise
on the limits to what must be attributed. The result is that the over-
whelming majority of influences that feed and enable any creative
work remain unattributed. Thus the re-use and non-attributive na-
tures of AI are not universal grounds to deny creativity, or accuse
it of plagiarism. We must first ask: are we applying the standards
of attribution appropriate to the context? What types of reuse are
we (in)visibilising? Do the authors of sources desire attribution?
```
## 2.5 Randomness as creativity

```
Randomness, or stochasticity, is an essential element of both the
training and generation phases of AI. Critics who argue against
the attribution of creativity to AI nonetheless note that random-
ness can be effectively used as a resource for producing creative
work, as in Cage’s “aleatoric compositions” [ 85 ] and Eno’s “oblique
strategies” [ 49 ]. In these practices, creativity comes not from the
random process itself, but from the way in which the artist uses it to
produce the resultant work. Blackwell writes [ 16 ]:“Tarot readings,
gambling, and other entertaining performances, just like the composi-
tions of John Cage, use random information as a starting point for
human creativity. But [...] random information is not communicating
anything [...] We can enjoy the performance of a Tarot reader, but the
```

```
CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany Advait Sarkar
```
idea that random events have meaning in themselves is nonsense. [...]
the same is true of the random processes that cause us to attribute
‘creativity’ to AI systems.”
Tarot, gambling, aleatoric composition, and oblique strategies are
all practices which draw explicitly on randomness as a resource for
creativity. Yet there are also many practices which, while they can be
viewed as random, are interpreted by practitioners as channelling
a different creative entity: the subconscious mind, the spirits of
ancestors, or religious beings.
The surrealist practice of “automatic writing”, drawing upon the
theories of Freud, aimed to produce writing without the interven-
tion of the conscious mind [ 100 ]. Practitioners of automatic writing
included W. B. Yeats and Arthur Conan Doyle. Automatic writers
either held a traditional writing instrument such as a pen, and at-
tempted to suppress their conscious processes while writing, or
used a specially prepared board such as a planchette. Later interpre-
tations of automatic writing aimed to channel not just the writer’s
subconscious, but to allow external spirits to guide the writer. This
spiritual interpretation borrowed from practices in other cultures,
such as Chinese Fuji spirit writing [ 63 ] for channelling various
deities (first recorded in the 5thcentury), medieval Christian glos-
solalia or “speaking in tongues” for channelling the holy spirit
[ 59 ], and American spiritualist talking boards (which evolved into
the well-known parlour game of Ouija boards) for channelling the
spirits of ancestors [ 94 ]. In each of these cases, the exercise is not
viewed as a human performance seeded by the random process, the
random process isitselfthe performance, given agency through
concepts such as the subconscious or spirits.
There might be a tendency for readers operating within con-
temporary Western ways of knowing to respond to examples such
as spirit writing and Ouija boards by denying their cultural in-
terpretation of being “extrinsic” to the human actors: “sure, spirit
writersclaimthey are not creating a performance, but inreality,
humans are still the true source of creativity, not any spirits.” This
is orientalist hubris. If we accept that definitions of creativity are
ultimately contextual and community-driven, we must also be open
to accepting community conceptions of the source(s) of creativity.
The stochastic nature of AI is not universal grounds to deny its
potential to be viewed by a practitioner community as a source of
creativity.

## 3 THE FORM-CONTENT DISTINCTION

In previous sections, we have implicitly encountered the idea that
there is a difference between form and content, or form and mean-
ing. When we considered how authorial intent and interpretation
can both affect meaning, it seems clear that the physical configura-
tion of words on a page, or pixels on a screen, is only part of what
determines the creative contribution (or plagiaristic nature) of a
work. Here there are more community-produced norms regarding
to what extent “form” determines content, and more fundamentally,
what the “unique form” of a work even is.

## 3.1 What is form?

What do we consider to be the “unique form” of a text? Is it a
certain configuration of letters or bits? Is each different occurrence
of the text, whether on screen as an array of coloured pixels, or

```
in ink printed on paper, a different form? In general we would
not consider two printed copies of the same text to be different
forms, despite the innumerable minute physical differences between
the copies, such as being printed on different paper, with slightly
different ink, etc. These differences are not relevant to our typical
determination of textual form, which generally relies on an abstract
notion of an arrangement of characters. A notion of “unique form”
centres around relevant and irrelevant differences. Unique forms
are separated from each other only by relevant differences. Forms
separated only by irrelevant differences have the same unique form.
But there is no notion of form universal to all texts. Change
the line breaks in a news article and it remains the same. Do the
same to a poem and the meaning changes. Change the typeface of
a school homework essay and it remains the same. Do the same to
a magazine advertisement and it is transformed. Some genres of
literature take this formalist emphasis to the extreme: “Concrete
poetry” celebrates the typographic form, showing how the arrange-
ment of letterforms can be used as a visual material, quite distinct
from the language semantics that arise when arranged into known
words. As Draper puts it [ 45 ],“the shaping of patterns takes pref-
erence over communication”. Similarly, “sound poetry” focuses on
the architectural configuration of phonetic speech sounds, rather
than the formation of words [ 111 ]. Concrete and sound poetry can
be viewed as prioritising “form over content”, yet they can also be
viewed as showing how a different kind of content can be created
out of form. This fascination for form-content subversion is not
limited to obscure corners of early 20thcentury poetry; to show
its enduring popularity one need only note the viral success of the
Netflix seriesIs It Cake?
In philosophy the issue of “type-token” distinction is related
[ 142 ]. The problem is that literary and art critics (or critics of AI
output) often talk about a work as an abstract form, or a type. Yet
“types” do not physically exist, only tokens – manifestations that we
can perceive. Philosophical scholars have variously characterised
types as sets, kinds, or laws, and have argued for both their exis-
tence and non-existence. The question for AI is this: each output
“token” (in the philosophical sense, not the natural language pro-
cessing sense), i.e., each time an output is displayed, is generally
not considered to be a novel creative act. If an AI’s output text is
copied and pasted form one application to another, or printed, these
various instances are generally all considered to be tokens of the
same original “type”, an attitude we inherit naturally from 21stcen-
tury knowledge work norms. In doing so we are implicitly choosing
some notion of “form” which may not be universally shared by all
human interpreters or appropriate for all contexts. This is relevant
when the work is being scrutinised for creativity or plagiarism.
If we choose a notion of form that is sensitive to line breaks, to
typeface, to materiality, etc., then these must be carried over from
the original token into any subsequently distributed copies, and we
must be aware of how the processes of copying and distribution
might introduce relevant formal (potentially creative) differences.
```
## 3.2 How much does form determine content?

```
Once a community has agreed suitable norms around what con-
stitutes form, there is the question of to what extent this form
```

```
The Impact of Artificial Intelligence on the Creativity of Knowledge Work CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany
```
determines content. In art and literary criticism (except with pro-
cedural and conceptual art), despite the enormous influence of
authorial intent and interpretation, form is generally considered
paramount to content. Change a line of a poem by Wordsworth, or
a soliloquy by Shakespeare, and the entire content is transformed.
Retelling the story of Romeo and Juliet in my own words is to not
convey Shakespeare at all, and would not be considered plagiarism
in the strictest sense. A rose by another name is another thing. A
restatement is a reinvention.
Contrast that to the way in which form is understood to relate
to content in academic writing. In this paper, like in all academic
writing, an idea is presented that is understood to be quite distinct
from the words used to convey it. This allows the community to
defend against a different kind of plagiarism during peer review:
“This idea was already published by X et al”. A restatement is not a
reinvention.
Art and literature harbour both extremes of form-content deter-
mination. On one extreme, where content is an idea quite abstracted
from form, is popular media. The popular conception of originality
tends to skew in preference to evaluating an abstract notion of con-
tent over a precise form. Critical television viewers, readers, and
moviegoers tend to reject storylines and tropes that are borrowed
wholesale from other popular works with which they are familiar,
recognising that the fundamental “idea” underneath is what counts,
not the way in which it is expressed. On the other extreme, where
content is entirely determined by a precise form, are writers like
Walter Benjamin. InThe Translator’s Task[ 12 ], Benjamin explains
that a translation – whose entire aim is ostensibly to achieve a
shift in form without a shift in content – is fundamentally impos-
sible:“translation is merely a preliminary way of coming to terms
with the foreignness of languages to each other. A dissolution of this
foreignness [...] remains out of human reach [...] the relation between
content and language in the original is entirely different from that in
the translation [... which] remains inappropriate, violent, and alien
with respect to its content [...] from outside it, facing it, and without
entering it, the translation calls to the original within, at that one
point where the echo in its own language can produce a reverberation
of the foreign language’s work”.
The line between form and content is precisely the one skirted
by knockoff brands, which evade legal action through clever modi-
fications of the legally formalised elements of brand identity, which
differ sufficiently from the original to render them nonequivalent
according to formal legal comparisons. On the other hand, the sim-
ilarities they retain allow them to still benefit from consumers’
mental association with the original brand.
Political activism has long exploited the ability to separate con-
tent from politically-controlled form. In 2022, Chinese lockdown
protesters were warned by the police not to ask for an end to
lockdowns. The crowd responded [ 139 ] by sarcastically chanting
“Continue lockdowns! [...] I want to do Covid tests!”Sarcasm reverses
the assumed content of form. Other protestors held up blank signs
in reference to a Soviet-era joke [ 2 , 32 ];“They know what they
want to express, and authorities know too, so people don’t need to
say anything. If you hold a blank sheet, then everyone knows what
you mean”. Context has the power to synthesise content from an
entirely absent form.

```
The interplay of form, context, intent, and interpretation in pro-
ducing content are key not just to political communication, but
innumerable instances of ordinary, everyday communication (as
noted in Grice’s theory of “implicatures” [ 62 ] and Miller’s theory
of explanations [ 96 ]). Indeed the study of this interplay is an entire
sub-field of linguistics [147].
In AI, influence of an idea in the training data may reveal itself
as what appears to be the same idea in content, but not in form.
Would this be considered plagiarism or creativity? A restatement
or a reinvention? The answer depends on which perspectives on
the form-content distinction we apply when evaluating the output.
Are we reading it as a poem, or a scientific paper? Are we applying
a popular conception of originality, or Walter Benjamin’s?
```
## 3.3 Labour, mechanisation, and creativity

```
Culturally produced form-content distinctions are nuanced and
resist generalisation, but I would cautiously suggest a recurrent
pattern: form-content distinctions (and therefore, distinctions of
creativity and originality) fall along the lines of mechanical repro-
duction. Where we see the labour of the human hand, we see a
difference in content. If a work is copied artfully by hand, the human
labour involved often grants it a new “aura” [ 11 ], an originality of its
own. When the medieval scribes copies a manuscript, or the sculp-
tor’s apprentice copies an original marble by his master, the copies
have intrinsic creative value despite their “formal” equivalence
to the original. But when a text is copied by print, or a sculpture
produced through a 3D printer, we see it as the same work as the
original. Today we are much less likely to consider a hand-copied
text to be different from the original than our medieval ancestors,
because our cultural attitudes to the value chain in text production
have been conditioned by centuries of the mechanisation of print.
The general (though not universal) principle is this: the lower
the marginal human labour of reproduction, the less we distinguish
the new forms as unique types, the more we see them as tokens
of the same general type. Mechanisation turns formerly relevant
differences in form, differences which arise or can be manipulated
through the mechanical process, into irrelevant differences. I be-
lieve the same principle is at play in the Japanese manga example at
the start of the paper: “classical” fan art is culturally acceptable be-
cause copying involves labour. AI-generated fan art is not, because
the form of copying it enables is not laborious in the same way.
Goldsmith notes that the huge quantitative increase in the speed of
copying enabled by computers resulted in the qualitative departure
of conceptual writing from earlier forms [ 1 ]:“previous forms of
borrowing in literature – collage or pastiche, taking a sentence from
here, a sentence from there – were predicated on the sheer amount of
manual labor involved: to retype an entire book is one thing, and to
cut and paste an entire book is another. The ease of appropriation has
raised the bar to a new level”.
Similarly, the launch of DeviantArt’s DreamUp AI art generation
service upset many artists due to its opt-in default [ 48 ]. Commen-
tary around the community reaction rejected the comparison of AI
art generation to collage, feeling that copying the style of an artist
was qualitatively different from collage. Artists’ own conceptions of
the fundamental injustice again centred on the labour requirements
of creating art in this new way: it feels more unjust, more like
```

```
CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany Advait Sarkar
```
```
copying, when it is made easy in comparison to familiar manual
methods. Artist Kelly McKernan said [ 144 ]:“I almost barely make
rent most months. I will spend, you know, 30 hours on a painting, and
I won’t see any money from that until it sells. [...] There’s more and
more [AI-generated] images that I can see my hand in, but it’s not my
work. I’m kind of feeling violated here. I’m really uncomfortable with
this”. Technological advances have repeatedly thrown into crisis
the ideals of creativity and labour in various artistic communities,
forcing their re-evaluation. In section 5 we will inspect how creativ-
ity is being re-evaluated in response to the challenge of AI, namely,
as a shift from material production to critical integration.
```
## 4 THE CHALLENGES OF INTELLECTUAL

## “PROPERTY”

It might seem helpful to look at legal definitions of originality and
creativity, e.g., those referenced in copyright law, to help understand
whether AI can be considered creative. The objective of this section
is to explain why it isnotas helpful as it may seem. The relatively
short history of intellectual property (IP) rights is essentially that
of the privatisation of thought as a capitalist instrument of control.
IP law has simultaneously been successful in furthering private
interests, while failing to capture a logically consistent notion of
creativity.
IP consists of legal devices such as copyrights, trademarks, patents,
etc. These are a relatively recent invention. For example, the first
recognisably modern copyright law was the English Statute of Anne
of 1710, which granted publishers the exclusive right to print a work
for 14 years after its first publication. It was introduced not out of
a desire to empower authors, as it was cleverly pitched at the time,
but rather to further the interests of powerful centralised printing
companies against cheaply made provincial and foreign books. Pat-
terson observes [ 110 ]:“The Statute of Anne [...] developed by and
for publishers, was clearly a publisher’s right, not an author’s right”.
The rights granted implicitly to authors in this statute were not
recognised in English common law until 1774, sixty-four years later.
Similarly, we can expect a new generation of legal devices invented
to manage the IP rights regarding AI output, and these will not at
first protect the entities we subsequently come to understand as
authors, but rather protect the most powerful lobbying voices.
Just as the privatisation of land forces people to sell labour in
order to eat [ 122 ], so the privatisation of thought functions as an
incentive to work in a knowledge economy. Pasquinelli explains the
motivation to pursue stronger intellectual property regimes bluntly
[ 109 ]:“copyright is one of the strategic evolutions of rent to expropriate
the cultural commons and reintroduce artificial scarcity. Speculation
then is directed toward intellectual property, forcing artificial costs
on cognitive goods that can paradoxically be reproduced or copied
virtually for free.”

## 4.1 Intellectual property’s dual agenda and

## reliance on notation

```
IP rights are a “negative right”: broadly speaking, the right to pre-
vent copying of creative ideas. This is a Western idea prioritising
the individual [ 127 ] based on the theory that if you protect people’s
ideas, they will innovate more, because they stand to protect their
financial gains. On the other hand, progress is cumulative and ideas
```
```
build on previous ideas, so one might expect that society will inno-
vate more if there are fewer IP laws. IP law therefore aims to strike a
balance between these two opposing tendencies. Economic models
and empirical analyses generally come to the intuitive conclusion
that some IP rights can improve innovation, but others can hinder
it [ 55 , 104 ]. IP rights therefore function more as a governmental
lever or dial for regulating innovation, like the interest rate of a
central bank, rather than as a quest for the legal enshrinement of
principled notions of creativity and ownership. Except that in order
to do so, it has entangled itself in this same quest.
The idea that one owns what one produces through one’s own
labour goes back to Locke [ 41 ]:“Whatsoever, then, he removes out
of the state that nature hath provided and left it in, he hath mixed
his labour with [...] and thereby makes it his property”. The related
labour theory of value developed by Smith, Ricardo (and then Marx)
appears somewhat later [ 41 ]. This is complicated by intellectual
property in two ways: first, the “labour” involved in producing an
idea is undefinable and unquantifiable, unlike the labour of pro-
ducing material goods. Secondly, labour alone appears insufficient
to qualify for ownership: if I labour to copy a poem written by
someone else, cultural norms around form and content in poetry
dictate that the idea for the poem does not now belong to me. Thus
copyright law in general rejects this “sweat of the brow” doctrine
and instead has to define a notion of originality, i.e., creativity [ 58 ].
This dual agenda of regulating innovation and defining creativity
is the source of many contradictions.
The main source of problems in the agenda of definition is its
reliance onnotation. For an idea to be apprehended by the legal
apparatus, for any judgement to be made regarding the equivalence
or nonequivalence of ideas, they must be notated in a way that
facilitates comparison. Selecting and developing a suitable notation
for the legal codification of ideas is the same as selecting a notion of
unique form, of deciding which differences are relevant and which
are irrelevant. Any particular choice of notation will inevitably
highlight certain aspects of ideas while ignoring others.
In the case of music copyright, courts note that a musical idea
must be written down in staff notation [ 80 ]. This inherits from the
specific ideals of the European Romantic composers of the 19th
century, that the composer’s notation expresses the true “intent”
of the music. Yet most genres of music across human cultures and
history, including the vast majority of contemporary music, is not
composed or amenable to notation in this way. This leads to ab-
surdities such as prohibiting jurors from listening to the music in
question [ 40 ], only looking at staff notation (which is transcribed
by a court-appointed notator, not the artists themselves) for deter-
mining equivalence and nonequivalence of musical ideas.
In response to the challenges of notation, courts will also employ
“ordinary observer” or “lay listener tests”, which amounts to play-
ing two pieces of music to the jury to assess if the compositions
“feel substantially” the same, while recognising the primacy of the
notational tests of equivalence. This leads to baffling and contradic-
tory procedures, such as the following [ 40 ]:“When the case returns
to trial, the jury will continue to not be able to hear [the] original
album recording [...] in order to judge its substantial similarity [...]
The jury will be able to hear the recording in order to weigh access,
but there might be measures in place to make sure the jury doesn’t
```

```
The Impact of Artificial Intelligence on the Creativity of Knowledge Work CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany
```
listen too closely”. Unsurprisingly, these tests draw criticism from
musicians and legal scholars alike, who note that lay listeners apply
inconsistent and easily biased criteria to judge musical similarity
[84, 89, 108].
Copyright law includes many exceptions and compromises to
paper over questions of form and content, such as the separation
of recording, composition, and performance rights, and the “idea-
expression” dichotomy [ 105 , 136 ], all of which are further problema-
tised by new modes of reproduction and performance enabled by
digitalisation. Copyright also includes various exceptions to cater
for the contextual nature of reuse (such as the “fair use” doctrine
which enables reuse for purposes such as education). These excep-
tions and contingencies are the result of intellectual property law
attempting to simultaneously act as a governmental lever for inno-
vation and as an arbiter of originality. The frail nature of copyright
comparisons is also vulnerable to absurd attacks such as Riehl’s
“All the Music” project [ 116 ], which has mechanically generated
all possible melodies 10 notes long and released it into the public
domain, to help musicians defend themselves against allegations of
copying.
The dual agenda of defining creativity and regulating innovation
requires arbitrary decisions to be made which can be influenced by
private interests. For example, time limits. Copyrights are not held
indefinitely: in the USA for instance, copyrights expire 70 years
after the death of the author. In what way has the creative nature of
the work changed on the first day of the 70thyear? The number 70 is
arbitrary, it has been changed several times, and is manipulated by
commercial interests. There is some evidence that the extensions to
US copyright protection periods in 1976 and 1998 were influenced
by lobbying from Disney, whose copyright on Mickey Mouse was
about to expire in each case [ 98 ]. Copyright draws arbitrary lines
in space as well as time: they are unevenly translated between the
jurisdictions of different countries, and they often have different
notational practices for determining equivalence. An idea that is
derivative on one side of the border magically becomes original on
the other side.
Another absurd episode in copyright law is the case of the in-
famous “monkey selfie” [ 117 ]. This was a dispute between British
photographer David Slater and the Wikimedia Foundation and
People for the Ethical Treatment of Animals (PETA). The dispute,
which lasted for seven years, centered around whether Slater held
the copyright to a photograph of an Indonesian crested macaque
that the macaque had “taken” of itself while manipulating Slater’s
camera. In the final ruling Slater was granted the copyright not be-
cause the courts determined that he was the source of the creativity
and originality in the image (it was clear that PETA was not actually
interested in the question of creativity but rather sought to raise
its own profile through a sensationalist lawsuit; we will see similar
attempts to grab headlines from companies eager to defend the
“rights” of AI), but on the rather less interesting technicality that
non-human actors are not entitled to copyright protection. But in
that case, corporations must not be entitled to copyright protection
either, because they are not humans. Yet corporations clearly do
hold copyrights. This apparent contradiction (and many others)
is resolved due to the legal standing of corporations as “artificial
persons”. This artificial personhood is what allows corporations to

```
be held accountable for actions, and some call for AI systems to
be given similar personhood to improve its accountability (though
there are criticisms of that approach [ 27 ]). Depending on whether
a particular AI system has been given legal personhood, it may or
may not be entitled to copyright protection under the current legal
regime, regardless of its creative role.
In the USA a war over electronic book lending is being waged
between librarians and publishers. With physical books, the library
purchases the book and then owns it forever. But they can only
lease electronic books for a certain period of time, after which the
lease needs to be renewed. This is an exorbitant recurring expense
which many libraries cannot afford. The publishers’ argument is
essentially that e-book lending makes it much easier for the public
to borrow books, which reduces sales. Yet this contradicts, or at
least undermines the spirit of the “first sale” doctrine of copyright,
which allows owners of copyrighted works (e.g., libraries) to lend,
sell, or share their copies without requiring permission or paying
additional fees [ 74 ]. The vastly reduced costs of replication and
distribution throw into crisis these notions of copyright, exposing
its basis as a practical, commercial mechanism, rather than any
universal notion of creativity and ownership.
```
## 4.2 Societal harms of legal definitions of

## creativity

```
The use of copyright to extract value from the creativity of minori-
ties and to deprive them of credit, compensation, and control, is
well documented [ 86 ]. Conversely, challenges to the notationally-
priveleged elite always emerge from marginalised communities.
The practices of DJ-ing and turntabling, from which the referential
practices of hip-hop and rap emerged, were forged in the devas-
tating fires of the South Bronx in the 1970s [ 77 ]. Artists with no
access to musical instruments or training made virtue of neces-
sity and turned their playback machines into musical instruments.
They echoed the emancipatory movements made by the cool, im-
provisational, quotational jazz of decades earlier, which drew on
black literary and musical traditions [ 101 ]. When marginalised com-
munities incorporate AI into their creative processes, we may see
similarly disrespectful and appropriational attitudes from the privi-
leged elite. The stochastic reuse nature of AI may be held against
marginalised communities in the same way that sampling or jazz
quotation struggles to defend its creativity in notationally-biased
courtrooms. We may see transnational conflicts with xenophobic
undertones, as exemplified in the attitudes of Western pharmaceu-
tical giants seeking to suppress the rights of Indian pharmaceutical
companies to manufacture affordable medicine [ 60 ], or the unfair
generalisation from a small set of bad actors to the branding of the
entire Chinese technology industry as being built upon IP theft
[83].
Copyright law is further complicated by the fact that copyright
of not just original but also “derivative works” is granted. This
opens up avenues for rent seeking. Many copyright lawsuits are
brought not by artists but by investment firms who have bought the
rights and seek to extract rent by proving “derivation”, essentially
the same business model as patent trolling. This has deleterious
effects on entire creative industries. The aftermath of the 2015
Blurred LinesandStay With Mecopyright lawsuits has profoundly
```

```
CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany Advait Sarkar
```
```
affected music production [ 126 ]. Many artists report feeling nervous
while composing, and fearful of trespassing into what they have
now been conditioned to see as the territory of previous artists.“I
shouldn’t be thinking about legal precedent when I am trying to write
a chorus”, said songwriter Evan Bogart [ 126 ]. New pre-emptive
citational practices have emerged, occasionally going as far as to
name influences as co-artists. Beyoncé’s 2022 singleBreak My Soul
credits Robin S.’s performance ofShow Me Love, despite clear and
notationally-defensible differences between the two songs [ 29 , 64 ].
Additional credits continued to be added and removed over time
[ 75 ]. Cautious over-attribution of this kind, and the consequential
payment of fractional royalties, seems to be anticipating, and hoping
to defuse, the crude approximate comparisons of the lay listener test.
Foucault noted how intellectual property laws in a slightly different
way, exerted a chilling effect on authorship, as when granted a
text as his “property” by copyright law, an author needed also to
bear the risks, including punishment for expressing transgressive
views [ 51 ]:“[The text’s] status as property is historically secondary
to the penal code controlling its appropriation [... prior to copyright
laws] books were assigned real authors [...] only when the author
became subject to punishment [... but] when a system of ownership
and strict copyright rules were established [... it restored] the danger
of writing”. The takeaway for AI is this: community-driven norms
for attribution can shift in response to the threat of legal action.
Attributional practices can be distorted by perceived threats and
thus become detached from notions of creativity and originality.
As far as musical creativity goes, the effort to establish universal,
fair, and logically consistent criteria for originality, equivalence,
and nonequivalence have largely failed. As the creative content of
AI generated works begins to undergo the same legal scrutiny, we
can be assured that the same jumbled mess of notations and tests
will continue to produce non-answers, and pressurise creative com-
munities to second-guess their creative workflows and attributional
practices.
```
## 4.3 Plagiarism or market-making?

As noted in the previous section on reuse: in the world of informa-
tion, a curatorial voice (Bush’s trail blazer) offers more value now
than ever before. The same has long been true of physical goods.
Shaviro [ 123 ] notes that Walmart, the world’s largest employer,
“focuses entirely upon circulation and distribution, rather than upon
old-style manufacturing — showing that the sphere of circulation
now (in contrast to Marx’s own time) plays a major role in the actual
extraction of surplus value”. A popular “get rich quick” scheme is
drop shipping (e.g., [ 65 ]). To start a drop shipping business, one sets
up a digital storefront through which customers can order various
goods. When an order comes in, the drop shipper purchases the
item “just in time” from another store, and orders it to be shipped
to the customer. This business works by price arbitrage: the drop
shipper simply purchases the good at a lower price, but sells it at a
higher price. The supplier is (usually) a Chinese producer with a
listing on a Chinese-language online retail store such as AliExpress.
The drop shipper’s storefront is designed to be attractive and claim
a certain level of luxury, often set up in English and aimed at Euro-
pean and North American markets. Unlike a retail distributor, the
drop shipper’s infrastructure and investments are minimal: there

```
are no real estate costs, no costs for maintaining inventory due to
the just in time approach, and negligible labour and operating costs
after deploying the online store. Entire businesses are built on the
premise of labelling cheap mass market commodities as luxuries,
such as the successful Daniel Wellington watch brand [114].
In (loose) economics terms, drop shippers can be interpreted as
providing value because they are market-makers [ 3 ]. They are ben-
efiting from the failure of the market to directly connect customers
to suppliers and offering an interface. On the flip side, they can be
viewed as exploiting the ignorance of the consumer, who could,
with a little effort, order the product at the lower price themselves,
and the ignorance of the supplier, who could, with a little effort, set
up their own similar storefront and charge the premium price them-
selves. In a similar manner, the copyright infringer, e.g., the seller
of unauthorised prints of books, or bootleg CDs, or pirated movies,
could be viewed as solving a market failure to bring a certain origi-
nal work to a certain viewer, or could be viewed as exploiting the
ignorance of the viewer and of the original source. In legal terms,
they are completely different scenarios. Drop shipping is legal and
seen as solving market problems. Copyright infringement is illegal
and seen to be exploitative. In terms of helping transport informa-
tion from source to end-consumer, they are identical. The difference
arises in theconsequencesof these activities for the various stake-
holders involved. For instance, drop shipping deprives the source of
only part of their potential revenue; piracy deprives them of all of
it. The consequence for AI is this: large language models and image
models can be viewed as a newly efficient method for connecting
the end-user with a space of information defined (partly) using a
training dataset. In some cases this facilitation of information flow
could be viewed as helpful market-making. In others it could be
viewed as exploitation.
In summary, this section has discussed the problems created
by the dual agenda of intellectual property rights and its reliance
on notation, and the numerous and unsatisfactory compromises
necessary to make such an agenda work in practice. For AI, the
implication is that relying on legal apparatus to help define cre-
ativity and plagiarism is subject to all the same compromises, and
simply furthers the private interests of powerful actors. As design-
ers of socio-technical systems, to appeal to legal arguments is to
knowingly abrogate responsibility to a failed project.
```
## 5 SHIFTING COMMUNITY NORMS FOR

## CREATIVITY IN AI-ASSISTED KNOWLEDGE

## WORK

```
So far we have considered many different conceptualisations of cre-
ativity, of form and notation, and the challenges of legal definitions.
I have suggested two patterns: first, that community is the ultimate
arbiter of creativity, and second, that community conceptions of
creativity often fall along the lines of mechanical (re)production. A
rapid fall in the cost of mechanical production in some parts of the
creative process causes communities to reconceptualise activities
such as art and writing to identify new sources of human value
and new loci of creativity. This section will briefly outline some
emergent patterns for where these new loci might sit according
to practitioner communities, based on studies of AI use in art and
writing.
```

```
The Impact of Artificial Intelligence on the Creativity of Knowledge Work CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany
```
## 5.1 From production to critical integration

AI models mechanise and thereby vastly reduce the cost of the
production of information, such as text or images. With further
advances in AI, the marginal human labour of material production,
of physically writing a text, or creating an image, will approach
zero. When it is mechanised, the process of material production will
cease to be viewed as creative. Instead, what we can observe is a
shift in knowledge work from production tocritical integration. The
output of AI systems will need to beintegratedinto a wider work-
flow involving human action. Creative labour is therefore expended
in deciding where in the workflow to use the productive power
of AI, how to program it correctly (e.g., in the current generation
of large language models this is done through “prompt engineer-
ing” [ 88 ]), and how to process its output in order to incorporate
it. This integration must becritical, meaning that creative labour
is expended in qualitative and expert human assessment of the
output, e.g., generated text might be checked for factual accuracy,
or generated code might be checked for correctness.
Some have likened this workflow to a “sandwich” [ 128 ], where
the human work of prompting and editing surrounds the AI gen-
eration process. Critical integration generalises the sandwich, if
you like, to the entire “double loop” [ 6 ] of critically reacting to
individual instances of AI use, and readjusting entire knowledge
workflows in response to meta-observations and hypotheses about
the roles AI might play. The concept of critical integration can be
illustrated through three studies, in creative writing, in visual arts,
and in programming.
First, Singh et al. studied how creative writing workflows shift
after the introduction of AI assistance [ 125 ]. In their study, AI
assistance was available continuously as the authors wrote and
took multiple forms: two different types of textual suggestions,
and suggested images and music retrieved from online databases
which were displayed/played ambiently within the editor. For us,
the most important observation they make in this study is that
AI-assisted writing consisted of “integrative leaps”, defined as“the
different kinds of interpretation and expression involved in incorpo-
rating aspects of suggestions into the developing story”. They identify
multiple axes of integration such as indirect-direct (to what extent is
an AI suggestion used as-is, without modification), and exploratory-
confirmatory (to what extent is an AI being used to continue the
current narrative, versus as a tool for exploring alternative narra-
tives). Participants were willing to attribute creativity to the AI
system (e.g.,“It was surprising to see the intelligence of the AI and
the creativeness of the suggestions”), yet still felt ownership of the
final text, because of the numerous authorial decisions required in
the course of critical integration (e.g.,“it helps me find an idea, but I
was the one who developed the story and make the story coherent”).
Second, Ploin et al. studied how AI tools affected the workflows
of a cohort of visual artists [ 113 ]. They found that artists engaged
in five new activities: studying AI to gain a better technical under-
standing, selecting/building/combining models, building datasets,
training models, and curating outputs. Artists made critical and
artistic judgements at every stage of the process. The analysis re-
veals a new community norm around creativity emerging, which
permits the creativity of production to be attributed to the system.

```
As one artist put it:“In the process, the model was entirely more cre-
ative than a human. It created images [...] I can’t create”. Yet the role
of critical integration, particularly integration of artwork into the
human-societal discourse of art, is a newly strengthened creative
responsibility of the artist. The artist continues:“The pictures of the
petals are beautiful [...] but it’s only made more meaningful by [...] a
human creator to contextualize and understand the present moment,
because art is created for people in a specific cultural moment”. Just as
with the Singh et al. study, the AI in these workflows is viewed as
its own intrinsic source of creativity whilesimultaneouslythe artist
performs the creative work of critical integration. As the authors
note,“creativity is an easier target than art”. Some creative work
can be fairly attributed to AI, but more creative work is required
to turn it into a knowledge product. Another artist said:“I believe
that these algorithms are and can be creative. [...] But there is a big
distinction between that and making art, or art that is interesting or
valid. That requires a lot of intentionality”.
Third, Sarkar et al. studied reports from programmers using AI
assistance for writing software code [ 120 ]. They too observe how
the creative work of writing code changes with AI assistance. It
shifts away from directly determining what character sequence ex-
presses the programmer’s intent and then physically typing it out.
It moves towards determining suitable prompts (“breaking down a
prompt at the ‘correct’ level of detail is also emerging as an important
developer skill”), identifying appropriate opportunities to use AI
assistance in the workflow (“this requires users to form a mental
model of when [AI] is likely to help them in their workflow. This
mental model takes time and intentionality to build [... programmers
are] constantly evaluating whether the current situation would benefit
from [AI] assistance”) and then critically evaluating and assimilat-
ing the output once generated (“developers need to learn new craft
practices for debugging”).
Besides the studies mentioned above, there have been many
other investigations of how contemporary generative AI supports
creative and knowledge work [ 30 , 33 , 39 , 57 , 69 , 95 , 97 , 107 , 132 , 134 ,
146 ]. Most of these studies provide empirical evidence or analytical
support for varying degrees of shift towards critical integration and
away from production, and show this shift to be a general pattern
across many different types of creative and knowledge work.
```
## 5.2 Implications of critical integration

```
In the wake of the release of ChatGPT, many were concerned about
the impact of AI on education, since writing textual answers and
essays forms so much of the “output” required by students over
the course of their learning careers [ 118 ]. What is the point in
learning to write if AI can do it for you? Some lamented this de-
velopment, while others were unruffled, pointing to the effect of
calculators on mental arithmetic. The shift to critical integration
suggests that perhaps editing and proofreading an AI-generated
essay becomes the new way of testing student skill, rather than the
material production of the words of the essay.
In the interim, what might be the implications of the shift to
critical integration for labour process issues, class relations, and
the agenda for HCI research and practice? These are important
questions which are largely out of scope for this paper; the focus
of this paper has been to explain the nature of critical integration
```

```
CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany Advait Sarkar
```
and to broaden the scope of discourse around AI and creativity in
knowledge work. However, it is worth briefly touching upon the
most salient issues. Braverman exposed the tendency of capitalism
to destroy craftsmanship and degrade work through Taylorism
[ 23 ], extending a Marxian analysis to the 20thcentury. Greenbaum
suggested that Computer-Supported Cooperative Work (CSCW)
research and technologies had been complicit in this degradation,
by enabling the transition from secure, well-paid “brick and mortar”
jobs to low-paid and precarious jobs that were nevertheless highly
skilled and challenging [ 61 ]. As an antidote, Greenbaum suggests
that designers and researchers explicitly consider the consequences
of a design agenda on labour, wages, and organisational structures,
using labour studies as a guide. He further suggests that they ought
to be held accountable for these consequences.
Just as Greenbaum claims CSCW research has contributed to
a Marxian breakdown of knowledge work and created new class
struggles and consolidation of capitalist power, so too do we need to
consider whether we are enabling these outcomes with generative
AI, or at least incorporate the labour process perspective from the
outset. Moreover, just because the community-produced definitions
of creativity might be shifting due to critical integration, and just
because material production can be automated, it does not follow
that everyone within a community wants it to be automated. The
implications for the class identity of knowledge work in response to
AI is too broad to be treated properly in this paper [ 76 , 91 ], though
it is of great importance to explore in future work.
However, we are still in a transitional phase, and it is unclear
how the technology will evolve and how society will evolve in
response. There are numerous examples of workflows in the early
industrial revolution that were not fully mechanised and were
repeatedly reconfigured over the course of decades as it became
possible to automate more and more of the workflow (or alter the
manufacturing objective to require less human intervention) [ 37 ].
McLuhan makes this point about printing:“Typography was no more
an addition to the scribal art than the motorcar was an addition to the
horse. Printing had its ‘horseless carriage’ phase of being misconceived
and misapplied during its first decades, when it was not uncommon
for the purchaser of a printed book to take it to a scribe to have it
copied and illustrated.”
It is harder still to anticipate how the fundamental enterprise of
knowledge work will shift in response to the challenge of AI in the
longer term. Perhaps critical integration is merely a stepping stone,
and future iterations of technology will successively erode the need
for human involvement in knowledge workflows in ever-increasing
proportion. In which case conducting knowledge work “by hand”
may for most become an activity for pleasure and recreation, or an
issue of class activism.

## 5.3 Resisting mechanised convergence through

## cultural reversal

In 1983 Bainbridge noted the ironies of a system that automates
“normal” operations while relying on human operators to step in to
handle exceptional situations and mitigate system errors [8]. This
is the situation we find ourselves in today, a complete reversal of
the 19thcentury motivations for developing computing machines
(articulated by Babbage and others [ 130 ]), which was to overcome

```
human errors. We have returned from “humans make errors, so
computers step in” to “computers make errors, so humans step in.”
This reversal was perhaps inevitable as we charged computers with
an increasingly broader and more complex set of tasks. McLuhan
notes many such examples of reversals that occur as a technology
matures or intensifies [93].
One tendency of mechanised production is the convergence of
expression to known and fixed forms. The printing press helped to
standardise spelling (though it is debated to what extent [ 24 , 68 ]),
much as spell check does today. Mass manufacturing standardised
many previously bespoke commodities, such as clothing. But when
this tendency for convergence is taken to an extreme, it becomes
repulsive. A clear example is the outcry surrounding Huawei’s
“Moon Mode” feature, which purported to use AI to improve the
clarity of pictures of the moon taken using the camera on the
Huawei P30 Pro smartphone. However, it emerged that the feature
worked by merging the user’s photograph with previously captured
higher resolution imagery [ 25 ]. On paper, it seems like a good idea:
it isthemoon, after all, and it is the same for everyone. But the
feature received severe criticism for failing to note a basic sentiment
that accompanies picture taking: the pride of personal possession.
This is why millions of tourists take terrible, blurry photographs of
the Taj Mahal and the Eiffel Tower each year despite the fact that
high resolution imagery is freely available online. Being connected
to the act of taking the photograph is more important than the
photograph itself, and this connection was severed by Moon Mode.
Per the Rifleman’s Creed:“There are many like it, but this one is
mine”.
The Moon Mode story is only one extreme example of a generally
more subtle tendency of AI to encourage a convergence of forms.
Studies find that writers who rely on predictive writing become
more predictable and less unique [ 7 ], and their opinions are influ-
enced by biases in the model [ 72 ]. The Moon Mode controversy (and
rising discontent against the increasingly opinionated and forceful
adjustments made by computational photography more generally
[ 31 ]) signals another cultural reversal. It pushes back against tech-
nological convergence of forms and says “no, I want this to bemy
picture”. The consumer movement to shop local and independent,
to consume indie music and cinema, is a countercultural reaction to
globalisation and the era of chain stores, supermarkets, and malls.
So too might we see consumer movements celebrating independent,
artisanal, and craft approaches to knowledge work. This prospect
of reversal is one reason to be optimistic that our AI future is not
one of institutionalised plagiarism and mindless repetition.
```
## 6 CONCLUSION

```
This position paper began by summarising the dominant view of
AI and creativity: that the output of AI systems, in information the-
oretic terms, cannot be considered creative because of its stochastic
reuse nature. We then viewed various alternative conceptions of cre-
ativity: as a process, as authorial intent, as interpretation, as reuse,
and as randomness – none of which is amenable to straightforward
analyses of information or notation. We discussed the multiple
equally valid positions one might adopt on the form-content dis-
tinction. We attended to the challenges of relying on intellectual
```

```
The Impact of Artificial Intelligence on the Creativity of Knowledge Work CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany
```
property law for analysing the creativity of AI. Two general pat-
terns were suggested: that creativity is determined contextually by
particular communities, and that sources of creativity in a workflow
are often determined by the extent to which different portions the
workflow are facilitated by mechanical means.
Finally, we looked to contemporary studies of AI-assisted cre-
ative knowledge work to glimpse how the loci of creativity are
shifting. It appears as though the human labour ofproductionis
being replaced by AI, while the opportunities for creative human
input have shifted tocritical integration, which is the assessment
of AI output and the set of authorial decisions required to incor-
porate that output into a knowledge workflow. The way in which
AI changes our relationship to the production of knowledge work
can be seen as analogous to how the industrial revolution changed
our relationship to material production. In response we reconfig-
ured our lives and social practices around the new machine-made
artefacts, and there was a long, arguably still ongoing period of
mutual accommodation between society and industrial technology.
It remains to be seen what will emerge from this new transitional
phase we find ourselves in. As such, the aim of this paper has been
to call for a broader, and more contextually-sensitive attitude to
what might constitute creativity in an age of human-AI knowledge
work.

## ACKNOWLEDGMENTS

Thanks to Alan Blackwell for discussions on the topic and reflec-
tions on drafts of the paper. Many thanks to my kind reviewers
whose suggestions have helped improve the paper.

## REFERENCES

```
[1]Kathy Acker, Noah Eli Gordon, Peter Gizzi, Tan Lin, Trisha Low, Juliana Spahr,
Bernadette Mayer, Harryette Mullen, Claudia Rankine, and Ron Silliman. 2011.
Against expression: an anthology of conceptual writing. Northwestern University
Press.
[2]Bruce Adams. 2005.Tiny revolutions in Russia: Twentieth century Soviet and
Russian history in anecdotes and jokes. Routledge.
[3]Yakov Amihud and Haim Mendelson. 1980. Dealership market: Market-making
with inventory.Journal of financial economics8, 1 (1980), 31–53.
[4]Nantheera Anantrasirichai and David Bull. 2022. Artificial intelligence in the
creative industries: a review.Artificial intelligence review(2022), 1–68.
[5] Maya Angelou. 1983. Caged bird.Shaker, why don’t you sing(1983), 9.
[6]Chris Argyris. 1977. Double loop learning in organizations.Harvard business
review55, 5 (1977), 115–125.
[7]Kenneth C Arnold, Krysta Chauncey, and Krzysztof Z Gajos. 2020. Predictive
text encourages predictable writing. InProceedings of the 25th International
Conference on Intelligent User Interfaces. 128–138.
[8]Lisanne Bainbridge. 1983. Ironies of automation. InAnalysis, design and evalua-
tion of man–machine systems. Elsevier, 129–135.
[9]Roland Barthes. 2016. The death of the author. InReadings in the Theory of
Religion. Routledge, 141–145.
[10]Emily M Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret
Shmitchell. 2021. On the Dangers of Stochastic Parrots: Can Language Models
Be Too Big?. InProceedings of the 2021 ACM conference on fairness, accountability,
and transparency. 610–623.
[11]Walter Benjamin. 1935. The Work of Art in the Age of Mechanical Reproduction,
1936.
[12]Walter Benjamin and Steven Rendall. 2021. The translator’s task. InThe
translation studies reader. Routledge, 89–97.
[13]Lionel Bently. 1994. Copyright and the Death of the Author in Literature and
Law.Mod. L. Rev.57 (1994), 973.
[14]Jonathan W Bernard. 1993. The minimalist aesthetic in the plastic arts and in
music.Perspectives of New Music(1993), 86–132.
[15]Alan F Blackwell. 2020. Objective functions:(In) humanity and inequity in
artificial intelligence.Science in the ForeSt, Science in the PaSt(2020), 191.
[16]Alan F. Blackwell. 2022. Coding or AI? Tools for Control, Surprise and Creativity.
InProceedings of the 33rd Annual Conference of the Psychology of Programming
```
```
Interest Group (PPIG 2022).
[17]Harold Bloom et al.1997.The anxiety of influence: A theory of poetry. Oxford
University Press, USA.
[18]Margaret Boden. 2008. Computers and creativity: models and applications.The
Routledge Companion to Creativity(2008), 179–188.
[19]Margaret A. Boden. 2007. Creativity in a nutshell.Think5, 15 (2007), 83–96.
https://doi.org/10.1017/S147717560000230X
[20]Margaret A Boden and Ernest A Edmonds. 2009. What is generative art?Digital
Creativity20, 1-2 (2009), 21–46.
[21]Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora,
Sydney von Arx, Michael S Bernstein, Jeannette Bohg, Antoine Bosselut, Emma
Brunskill, et al.2021. On the opportunities and risks of foundation models.
arXiv preprint arXiv:2108.07258(2021).
[22] Jorge Luis Borges. 1962.Ficciones. Vol. 320. Grove Press.
[23]Harry Braverman. 1998.Labor and monopoly capital: The degradation of work in
the twentieth century. NYU Press.
[24]Fred H Brengelman. 1980. Orthoepists, printers, and the rationalization of
English spelling.The Journal of English and Germanic Philology79, 3 (1980),
332–354.
[25]C. Scott Brown. 2019. Huawei P30 Pro ’Moon Mode’ stirs controversy (update:
Huawei responds). https://www.androidauthority.com/huawei-p30-pro-moon-
mode-controversy-978486/
[26]Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan,
Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al.2020. Language models are few-shot learners.Advances in neural
information processing systems33 (2020), 1877–1901.
[27]Joanna J Bryson, Mihailis E Diamantis, and Thomas D Grant. 2017. Of, for, and
by the people: the legal lacuna of synthetic persons.Artificial Intelligence and
Law25 (2017), 273–291.
[28]Vannevar Bush et al.1945. As we may think.The atlantic monthly176, 1 (1945),
101–108.
[29]Paul Cantor. 2022. Did Beyonce really sample Robin S "Show me love" on New
Song "Break My Soul"? https://paulcantor.medium.com/did-beyonce-really-
sample-robin-s-show-me-love-on-new-song-break-my-soul-9cbf1d4b626a
[30]Baptiste Caramiaux and Sarah Fdili Alaoui. 2022. " Explorers of Unknown
Planets" Practices and Politics of Artificial Intelligence in Visual Arts.Proceedings
of the ACM on Human-Computer Interaction6, CSCW2 (2022), 1–24.
[31]Kyle Chayka. 2022. Have iphone cameras become too smart?
https://www.newyorker.com/culture/infinite-scroll/have-iphone-cameras-
become-too-smart
[32]Chang Che and Amy Chang Chien. 2022. Memes, puns and blank sheets of
paper: China’s creative acts of protest. https://www.nytimes.com/2022/11/28/
world/asia/china-protests-blank-sheets.html
[33]John Joon Young Chung, Shiqing He, and Eytan Adar. 2022. Artist support net-
works: Implications for future creativity support tools. InDesigning Interactive
Systems Conference. 232–246.
[34]Alexander Clement. 2018.Brutalism: post-war British architecture. The Crowood
Press.
[35]Harry M Collins, Martin Kusch, et al.1998.The shape of actions: What humans
and machines can do. MIT press.
[36]Mary-Ann Constantine. 2019. 79The possibilists: Romantic-era lit-
erary forgery and British alternative pasts. InCounterfactual Ro-
manticism. Manchester University Press. https://doi.org/10.7765/
9781526107077.00009 arXiv:https://academic.oup.com/manchester-
scholarship-online/book/0/chapter/262463140/chapter-ag-
pdf/44552686/book_30839_section_262463140.ag.pdf
[37]Jason Crawford. 2018. Out of whole cloth. https://rootsofprogress.org/out-of-
whole-cloth
[38]Christina Currie and Dominique Allart. 2012. Pieter Brueghel as a copyist after
Pieter Bruegel. (2012).
[39]Hai Dang, Karim Benharrak, Florian Lehmann, and Daniel Buschek. 2022. Be-
yond Text Generation: Supporting Writers with Continuous Automatic Text
Summaries. InProceedings of the 35th Annual ACM Symposium on User Interface
Software and Technology. 1–13.
[40]Jordan Davis. 2018. 9th Circuit Orders Retrial Over “Stairway to Heaven”
Copyright Infringement Case. (2018).
[41]John P Day. 1966. Locke on property.The Philosophical Quarterly (1950-)16, 64
(1966), 207–220.
[42]Guy Debord and Gil J Wolman. 1956. Methods of detournement.Les Lèvres
Nues8 (1956).
[43]Andrew Deck. 2022. Ai-generated art sparks furious backlash from Japan’s
Anime Community. https://restofworld.org/2022/ai-backlash-anime-artists/
[44]Daniel C Dennett. 1971. Intentional systems.The Journal of Philosophy68, 4
(1971), 87–106.
[45]Ronald P Draper. 1971. Concrete poetry.New Literary History2, 2 (1971),
329–340.
[46]Peter F. Drucker. 1959.Landmarks of Tomorrow(1st ed. ed.). Harper, New York.
```

CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany Advait Sarkar

```
[47]Jennifer Duggan. 2022. Transformative readings: Harry Potter fan fiction,
trans/queer reader response, and JK Rowling.Children’s Literature in Education
53, 2 (2022), 147–168.
[48]Benj Edwards. 2022. DeviantArt upsets artists with its new AI Art Gener-
ator, DreamUp. https://arstechnica.com/information-technology/2022/11/
deviantart-upsets-artists-with-its-new-ai-art-generator-dreamup/
[49]Brian Eno and Peter Schmidt. 1975. Oblique strategies.Opal.(Limited edition,
boxed set of cards.)[rMAB](1975).
[50]Kirby Ferguson. 2022. Everything is a remix. https://www.everythingisaremix.
info/
[51] Michel Foucault. 2017. What is an Author? InAesthetics. Routledge, 284–288.
[52]Jonas Frich, Michael Mose Biskjaer, and Peter Dalsgaard. 2018. Twenty years of
creativity research in human-computer interaction: Current state and future
directions. InProceedings of the 2018 Designing Interactive Systems Conference.
1235–1257.
[53] Wayne J Froman. 1988. Action painting and the world-as-picture.The Journal
of aesthetics and art criticism46, 4 (1988), 469–475.
[54]David W Galenson. 2011. Old masters and young geniuses. InOld Masters and
Young Geniuses. Princeton University Press.
[55]Kausik Gangopadhyay and Debasis Mondal. 2012. Does stronger protection
of intellectual property stimulate innovation?Economics Letters116, 1 (2012),
80–82.
[56]William Gaver. 2012. What should we expect from research through design?.
InProceedings of the SIGCHI conference on human factors in computing systems.
937–946.
[57]Katy Ilonka Gero, Vivian Liu, and Lydia Chilton. 2022. Sparks: Inspiration
for science writing using language models. InDesigning Interactive Systems
Conference. 1002–1019.
[58]Jane C Ginsburg. 1992. No Sweat Copyright and Other Protection of Works of
Information after Feist v. Rural Telephone.Colum. L. Rev.92 (1992), 338.
[59]Felicitas D Goodman. 2008.Speaking in tongues: A cross-cultural study of glosso-
lalia. Wipf and Stock Publishers.
[60]Cheri Grace. 2004. The effect of changing intellectual property on pharmaceuti-
cal industry prospects in India and China.DFID Health Systems Resource Centre
(2004), 1–68.
[61]Joan Greenbaum. 1996. Back to Labor: Returning to labor process discussions
in the study of work. InProceedings of the 1996 ACM conference on Computer
supported cooperative work. 229–237.
[62] Herbert P Grice. 1975. Logic and conversation. InSpeech acts. Brill, 41–58.
[63]Jan Jakob Maria Groot. 1964.The religious system of China. Vol. 4. Brill Archive.
[64]Charlie Harding. 2022. Beyoncé’s House. https://switchedonpop.com/episodes/
beyonce-house-break-my-soul-show-me-love
[65]Mark Hayes and Andrew Youderian. 2013.The ultimate guide to dropshipping.
Lulu. com.
[66]Mickey Hess. 2006. Was Foucault a plagiarist? Hip-hop sampling and academic
citation.Computers and Composition23, 3 (2006), 280–295.
[67]Charlotte Higgins. 2004. Work of art that inspired a movement ... a urinal.
https://www.theguardian.com/uk/2004/dec/02/arts.artsnews
[68]Trevor Howard Howard-Hill. 2006. Early modern printers and the standardiza-
tion of English spelling.Modern Language Review101, 1 (2006), 16–29.
[69]Nanna Inie, Jeanette Falk, and Steven Tanimoto. 2023. Designing Participatory
AI: Creative Professionals’ Worries and Expectations about Generative AI.arXiv
preprint arXiv:2303.08931(2023).
[70]William Irwin. 2015. Authorial declaration and extreme actual intentionalism:
Is Dumbledore gay?The Journal of Aesthetics and Art Criticism73, 2 (2015),
141–147.
[71] Wolfgang Iser and Jane Tompkins. 1984.Reader-response criticism.
[72]Maurice Jakesch, Advait Bhat, Daniel Buschek, Lior Zalmanson, and Mor Naa-
man. 2023. Co-Writing with Opinionated Language Models Affects Users’ Views.
arXiv preprint arXiv:2302.00560(2023).
[73]Alison James. 2009.Constraining Chance: Georges Perec and the Oulipo. North-
western University Press.
[74]Jennifer Jenkins. 2014. Last sale?: Libraries’ rights in the digital age.College &
Research Libraries News75, 2 (2014), 69–75.
[75]Rich Juzwiak. 2022. Beyoncé’s ’Break My Soul’ and the Long Tail of ’Show Me
Love’. https://www.nytimes.com/2022/06/27/arts/music/beyonce-break-my-
soul-robin-s-show-me-love.html
[76]Emrah Karakilic. 2022. Why do humans remain central to the knowledge
work in the age of robots? Marx’s Fragment on machines and beyond.Work,
Employment and Society36, 1 (2022), 179–189.
[77]Mark Katz. 2012.Groove music: The art and culture of the hip-hop DJ. Oxford
University Press on Demand.
[78]Alison Kidd. 1994. The marks are on the knowledge worker. InProceedings of
the SIGCHI conference on Human factors in computing systems. 186–191.
[79]Oksana Kopenkina. 2022. Pieter Bruegel the younger. copyist or great artist? -
arts diary & PAD. https://arts-pad.com/pieter-bruegel-the-younger/
[80]Susan J Latham. 2003. Newton v. Diamond; Measuring the Legitimacy of Unau-
thorized Compositional Samplling-A Clue Illuminated and Obscured.Hastings
```
```
Comm. & Ent. LJ26 (2003), 119.
[81]MoMA Learning. 2023. Marcel Duchamp and the Readymade.
https://www.moma.org/learn/moma_learning/themes/dada/marcel-duchamp-
and-the-readymade/
[82]Jooyoung Lee, Thai Le, Jinghui Chen, and Dongwon Lee. 2022. Do Language
Models Plagiarize?arXiv preprint arXiv:2203.07618(2022).
[83]Kai-Fu Lee. 2018.AI superpowers: China, Silicon Valley, and the new world order.
Houghton Mifflin.
[84]Mark A Lemley. 2009. Our Bizarre System for Proving Copyright Infringement.
J. Copyright Soc’y USA57 (2009), 719.
[85]Tuck Wah Leong, Frank Vetere, and Steve Howard. 2006. Randomness as a
resource for design. InProceedings of the 6th conference on Designing Interactive
systems. 132–139.
[86]Toni Lester. 2013. Blurred Lines-Where Copyright Ends and Cultural Appropri-
ation Begins-The Case of Robin Thicke versus Bridgeport Music and the Estate
of Marvin Gaye.Hastings Comm. & Ent. LJ36 (2013), 217.
[87] Sol LeWitt. 1967. Paragraphs on conceptual art.Artforum5, 10 (1967), 79–83.
[88]Vivian Liu and Lydia B Chilton. 2022. Design guidelines for prompt engineering
text-to-image generative models. InProceedings of the 2022 CHI Conference on
Human Factors in Computing Systems. 1–23.
[89]Jamie Lund. 2011. An empirical examination of the lay listener test in music
composition copyright infringement.Va. Sports & Ent. LJ11 (2011), 137.
[90]Adrian Mackenzie. 2017.Machine learners: Archaeology of a data practice. MIT
Press.
[91]Abigail Marks and Chris Baldry. 2009. Stuck in the middle with who? The class
identity of knowledge workers.Work, Employment and Society23, 1 (2009),
49–65.
[92]Ilana Masad. 2016. Harry Potter and the possible queerbaiting: Why fans are mad
over a lack of gay romance. https://www.theguardian.com/books/booksblog/
2016/aug/16/harry-potter-possible-example-queerbaiting-cursed-child
[93]Marshall McLuhan. 1994.Understanding media: The extensions of man. MIT
press.
[94]Linda Rodriguez McRobbie. 2013. The strange and mysterious history of the
Ouija board. https://www.smithsonianmag.com/history/the-strange-and-
mysterious-history-of-the-ouija-board-5860627/
[95]Arthur I Miller. 2019.The artist in the machine: The world of AI-powered creativity.
Mit Press.
[96]Tim Miller. 2019. Explanation in artificial intelligence: Insights from the social
sciences.Artificial intelligence267 (2019), 1–38.
[97]Piotr Mirowski, Kory W Mathewson, Jaylen Pittman, and Richard Evans. 2022.
Co-writing screenplays and theatre scripts with language models: An evaluation
by industry professionals.arXiv preprint arXiv:2209.14958(2022).
[98]Viva R Moffat. 2004. Mutant copyrights and backdoor patents: the problem of
overlapping intellectual property protection.Berkeley Tech. LJ19 (2004), 1473.
[99] Yann Moulier-Boutang. 2011.Cognitive capitalism. Polity.
[100] Anita Mary Mühl. 1930.Automatic writing. T. Steinkopff.
[101]John P Murphy. 1990. Jazz improvisation: The joy of influence.The black
perspective in music(1990), 7–19.
[102]Marcello Musto. 2010. Revisiting Marx’s concept of alienation.Socialism and
Democracy24, 3 (2010), 79–101.
[103]Marcello Musto. 2015. The ‘Young Marx’Myth in interpretations of the
economic–philosophic manuscripts of 1844.Critique43, 2 (2015), 233–260.
[104]Pedro Cunha Neves, Oscar Afonso, Diana Silva, and Elena Sochirca. 2021. The
link between intellectual property rights, innovation, and growth: A meta-
analysis.Economic Modelling97 (2021), 196–209.
[105]Jon O Newman. 1999. New lyrics for an old melody: The idea/expression
dichotomy in the computer age.Cardozo Arts & Ent. LJ17 (1999), 691.
[106]Anthony David Nuttall. 1968. Did Meursault mean to kill the Arab?-The Inten-
tional Fallacy Fallacy.Critical Quarterly10, 1-2 (1968), 95–106.
[107]Jonas Oppenlaender. 2022. The Creativity of Text-to-Image Generation. In
Proceedings of the 25th International Academic Mindtrek Conference. 192–202.
[108]Jason Palmer. 2015. Blurred Lines Means Changing Focus: Juries Composed of
Musical Artists Should Decide Music Copyright Infringement Cases, Not Lay
Juries.Vand. J. Ent. & Tech. L.18 (2015), 907.
[109]Matteo Pasquinelli. 2009. Google’s PageRank algorithm: A diagram of cognitive
capitalism and the rentier of the common intellect.Deep search: The politics of
search beyond Google(2009), 152–162.
[110]Lyman Ray Patterson. 1965. The Statute of Anne: Copyright Misconstrued.
Harv. J. on Legis.3 (1965), 223.
[111]Marjorie Perloff and Craig Dworkin. 2009.The Sound of Poetry/The Poetry of
Sound. University of Chicago Press.
[112] Tom Phillips et al. 1987. A humument. (1987).
[113]A. Ploin, R. Eynon, Hjorth I., and M.A. Osborne. 2022.AI and the Arts: How Ma-
chine Learning is Changing Artistic Work. Report from the Creative Algorithmic
Intelligence Research Project. Oxford Internet Institute, University of Oxford,
UK.
[114]Stephen Pulvirent. 2015. How Daniel Wellington made a $200 million business
out of cheap watches. https://www.bloomberg.com/news/articles/2015-07-14/
```

The Impact of Artificial Intelligence on the Creativity of Knowledge Work CHIWORK 2023, June 13–16, 2023, Oldenburg, Germany

how-daniel-wellington-made-a-200-million-business-out-of-cheap-watches
[115]Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Rad-
ford, Mark Chen, and Ilya Sutskever. 2021. Zero-shot text-to-image generation.
InInternational Conference on Machine Learning. PMLR, 8821–8831.
[116] Damien Riehl. 2020. All the Music. [http://allthemusic.info/faqs/](http://allthemusic.info/faqs/)
[117]Eleonora Rosati. 2017. The Monkey Selfie case and the concept of authorship:
an EU perspective.Journal of Intellectual Property Law & Practice12, 12 (2017),
973–977.
[118]Jürgen Rudolph, Samson Tan, and Shannon Tan. 2023. ChatGPT: Bullshit spewer
or the end of traditional assessments in higher education?Journal of Applied
Learning and Teaching6, 1 (2023).
[119]Advait Sarkar. 2023. Enough With "Human-AI Collaboration". InExtended
Abstracts of the 2023 CHI Conference on Human Factors in Computing Systems
(CHI EA 2023).
[120]Advait Sarkar, Andrew D. Gordon, Carina Negreanu, Christian Poelitz, Sruti
Srinivasa Ragavan, and Ben Zorn. 2022. What is it like to program with artificial
intelligence?. InProceedings of the 33rd Annual Conference of the Psychology of
Programming Interest Group (PPIG 2022).
[121]Joseph G Schloss. 2014.Making beats: The art of sample-based hip-hop. Wesleyan
University Press.
[122]Augustine Sedgewick. 2021.Coffeeland: One Man’s Dark Empire and the Making
of Our Favorite Drug. Penguin.
[123]Steven Shaviro. 2008. Cognitive capitalism? [http://www.shaviro.com/Blog/?p=](http://www.shaviro.com/Blog/?p=)
620
[124]Dean Keith Simonton. 2012. Taking the US Patent Office criteria seriously: A
quantitative three-criterion creativity definition and its implications.Creativity
research journal24, 2-3 (2012), 97–106.
[125]Nikhil Singh, Guillermo Bernal, Daria Savchenko, and Elena L Glassman. 2022.
Where to hide a stolen elephant: Leaps in creative writing with multimodal
machine intelligence.ACM Transactions on Computer-Human Interaction(2022).
[126]Ben Sisario. 2019. ’blurred lines’ on their minds, songwriters create ner-
vously. https://www.nytimes.com/2019/03/31/business/media/plagiarism-
music-songwriters.html
[127]Linda Tuhiwai Smith. 2021.Decolonizing methodologies: Research and indigenous
peoples. Bloomsbury Publishing.
[128]Noah Smith. 2022. Generative AI: Autocomplete for everything. https://
noahpinion.substack.com/p/generative-ai-autocomplete-for-everything
[129] Stephen Smith. 2006.An inkwell of pen names. Xlibris Corporation.
[130]Laura J Snyder. 2011.The philosophical breakfast club: four remarkable friends
who transformed science and changed the world. Crown.
[131] Susan Sontag et al. 1994.Against interpretation. Vintage London.
[132]Minhyang Suh, Emily Youngblom, Michael Terry, and Carrie J Cai. 2021. Ai
as social glue: Uncovering the roles of deep generative ai during social music
composition. InProceedings of the 2021 CHI conference on human factors in
computing systems. 1–11.
[133]H. Holden Thorp. 2023. ChatGPT is fun, but not an author. Sci-
ence379, 6630 (2023), 313–313. https://doi.org/10.1126/science.adg
arXiv:https://www.science.org/doi/pdf/10.1126/science.adg
[134]Imke van Heerden and Anil Bas. 2021. Ai as author–bridging the gap between
machine learning and literary theory.Journal of Artificial Intelligence Research
71 (2021), 175–189.
[135]Cedric VanEenoo. 2011. Minimalism in Art and Design: Concept, influences,
implications and perspectives.Journal of Fine and Studio Art2, 1 (2011), 7–12.
[136]Simonetta Vezzoso. 2012. Copyright, Interfaces, and a Possible Atlantic Divide.
J. Intell. Prop. Info. Tech. & Elec. Com. L.3 (2012), 153.
[137] Graham Wallas. 1926.The art of thought. Vol. 10. Harcourt, Brace.
[138]Kai Wang and Jeffrey V Nickerson. 2017. A literature review on individual
creativity support systems.Computers in Human Behavior74 (2017), 139–151.
[139]Vivian Wang. 2022. A protest? A vigil? in Beijing, anxious crowds are unsure
how far to go. https://www.nytimes.com/2022/11/28/world/asia/china-protests-
covid-beijing.html
[140]Laura Weidinger, John Mellor, Maribeth Rauh, Conor Griffin, Jonathan Uesato,
Po-Sen Huang, Myra Cheng, Mia Glaese, Borja Balle, Atoosa Kasirzadeh, et al.

2021. Ethical and social risks of harm from language models.arXiv preprint
arXiv:2112.04359(2021).
[141]Elizabeth Weil. 2023. You are not a parrot. https://nymag.com/intelligencer/
article/ai-artificial-intelligence-chatbots-emily-m-bender.html
[142]Linda Wetzel. 2018. Types and Tokens. InThe Stanford Encyclopedia of Philosophy
(Fall 2018 ed.), Edward N. Zalta (Ed.). Metaphysics Research Lab, Stanford
University.
[143]William Kurtz Wimsatt and Monroe Curtis Beardsley. 1946. The intentional
fallacy.The sewanee review54, 3 (1946), 468–488.
[144]Darian Woods and Adrian Ma. 2023. Artists vs. AI. https://www.npr.org/
transcripts/
[145]Tianna Xu, Advait Sarkar, and Sean Rintel. 2023. Is a Return To Office a Return
To Creativity? Requiring Fixed Time In Office To Enable Brainstorms and Water-
cooler Talk May Not Foster Research Creativity(CHIWORK 2023). Association
for Computing Machinery, New York, NY, USA.

```
[146]Daijin Yang, Yanpeng Zhou, Zhiyuan Zhang, Toby Jia-Jun Li, and Ray LC. 2022.
AI as an Active Writer: Interaction strategies with generated text in human-AI
collaborative fiction writing. InJoint Proceedings of the ACM IUI Workshops,
Vol. 10.
[147] George Yule and HG Widdowson. 1996.Pragmatics. Oxford university press.
[148]John Zimmerman, Jodi Forlizzi, and Shelley Evenson. 2007. Research through
design as a method for interaction design research in HCI. InProceedings of the
SIGCHI conference on Human factors in computing systems. 493–502.
```
```
Received 20 February 2007; revised 12 March 2009; accepted 5 June 2009
```

