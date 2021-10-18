<ul class="tabs-content mb-0 min-h-[200px] h-auto md:h-[calc(100vh-195px)] overflow-auto"><li class="is-active md:h-full" data-tab="description"><div class="description is-full-height has-auto-scrolling p-4"><div class="markdown prose max-w-none" id="description"><p>Write a function that, given a string of text (possibly with punctuation and line-breaks),
returns an array of the top-3 most occurring words, in descending order of the number of occurrences.</p>
<h2 id="assumptions">Assumptions:</h2>
<ul>
<li>A word is a string of letters (A to Z) optionally containing one or more apostrophes (<code>'</code>) in ASCII.</li>
<li>Apostrophes can appear at the start, middle or end of a word (<code>'abc</code>, <code>abc'</code>, <code>'abc'</code>, <code>ab'c</code> are all valid)</li>
<li>Any other characters (e.g. <code>#</code>, <code>\</code>, <code>/</code> , <code>.</code> ...) are not part of a word and should be treated as whitespace.</li>
<li>Matches should be case-insensitive, and the words in the result should be lowercased.</li>
<li>Ties may be broken arbitrarily.</li>
<li>If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.</li>
</ul>
<h2 id="examples">Examples:</h2>
<pre><code>top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# =&gt; ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")

# =&gt; ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")

# =&gt; ["won't", "wont"]

</code></pre>
<h2 id="bonus-points-not-really-but-just-for-fun">Bonus points (not really, but just for fun):</h2>
<ol>
<li>Avoid creating an array whose memory footprint is roughly as big as the input text.</li>
<li>Avoid sorting the entire array of unique words.</li>
</ol>
</div><hr><div class="mt-15px"><span><i class="icon-moon-tag "></i></span><div class="keyword-tag">Algorithms</div><div class="keyword-tag">Strings</div><div class="keyword-tag">Parsing</div><div class="keyword-tag">Ranking</div><div class="keyword-tag">Filtering</div></div><hr><br><div class="text-center"><a class="hover:text-current" data-tippy-content="Supercharge your technical hiring with developer assessments." data-tippy-placement="top" href="https://www.qualified.io?utm_source=codewars&amp;utm_medium=web" rel="noopener" target="_blank"><div class="flex items-baseline justify-center"><span class="pl-1 text-xs inline-block">powered by</span><img class="h-4 inline-block dark:hidden pl-1" src="/assets/logos/qualified-black-b052752a4beaf94810c9d982f495680e2a9eb207824764ef98240ccef15cfbb1.svg"><img class="h-4 hidden dark:inline-block pl-1" src="/assets/logos/qualified-white-7cba1bde874154ee4f39d50aebd5b7e435f5b21af9884b236a60d9015039e7f0.svg"></div></a></div></div></li><li class="md:h-full is-overflow-hidden" data-tab="output"><div class="console-output is-full-height p-0"><div class="is-full-height" id="code_results"><div class="alert-box no-border is-square mb-0 is-full-height"><div class="message"><i class="icon-moon-info "></i>Your output will be shown here</div><iframe data-src="https://cr.codewars.com?api=v2&amp;utm_campaign=kata_trainer&amp;utm_medium=web&amp;utm_source=codewars#congrats=true&amp;pro=false&amp;theme=dark" id="runner_frame" sandbox="allow-scripts allow-same-origin allow-pointer-lock" src="https://cr.codewars.com?api=v2&amp;utm_campaign=kata_trainer&amp;utm_medium=web&amp;utm_source=codewars#congrats=true&amp;pro=false&amp;theme=dark"></iframe></div></div></div></li><li class="md:h-full is-overflow-auto" data-tab="solutions"><div class="is-full-height mb-15px p-15px"></div></li></ul>