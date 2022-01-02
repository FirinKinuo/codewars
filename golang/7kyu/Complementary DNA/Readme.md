<div class="description is-full-height has-auto-scrolling p-4"><div class="markdown prose max-w-none" id="description"><p>Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.</p>
<p>If you want to know more: <a href="http://en.wikipedia.org/wiki/DNA" target="_blank">http://en.wikipedia.org/wiki/DNA</a></p>
<p>In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).</p>
<p>More similar exercise are found here: <a href="http://rosalind.info/problems/list-view/" target="_blank">http://rosalind.info/problems/list-view/</a> (source)</p>
<p>Example: (<strong>input --&gt; output</strong>)</p>
<pre><code>"ATTGC" --&gt; "TAACG"
"GTAT" --&gt; "CATA"
</code></pre>
<pre><code class="language-if-haskell">dnaStrand []        `shouldBe` []
dnaStrand [A,T,G,C] `shouldBe` [T,A,C,G]
dnaStrand [G,T,A,T] `shouldBe` [C,A,T,A]
dnaStrand [A,A,A,A] `shouldBe` [T,T,T,T]
</code></pre></div>
