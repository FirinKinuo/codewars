<div class="markdown prose max-w-none" id="description"><p>This time we want to write calculations using functions and get the results. Let's have a look at some examples:</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">seven</span>(<span class="cm-variable">times</span>(<span class="cm-variable">five</span>())); <span class="cm-comment">// must return 35</span>
<span class="cm-variable">four</span>(<span class="cm-variable">plus</span>(<span class="cm-variable">nine</span>())); <span class="cm-comment">// must return 13</span>
<span class="cm-variable">eight</span>(<span class="cm-variable">minus</span>(<span class="cm-variable">three</span>())); <span class="cm-comment">// must return 5</span>
<span class="cm-variable">six</span>(<span class="cm-variable">dividedBy</span>(<span class="cm-variable">two</span>())); <span class="cm-comment">// must return 3</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">seven</span>(<span class="cm-variable">times</span>(<span class="cm-variable">five</span>)) <span class="cm-comment"># must return 35</span>
<span class="cm-variable">four</span>(<span class="cm-variable">plus</span>(<span class="cm-variable">nine</span>)) <span class="cm-comment"># must return 13</span>
<span class="cm-variable">eight</span>(<span class="cm-variable">minus</span>(<span class="cm-variable">three</span>)) <span class="cm-comment"># must return 5</span>
<span class="cm-variable">six</span>(<span class="cm-variable">divided_by</span>(<span class="cm-variable">two</span>)) <span class="cm-comment"># must return 3</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">seven</span>(<span class="cm-variable">times</span>(<span class="cm-variable">five</span>())) <span class="cm-comment"># must return 35</span>
<span class="cm-variable">four</span>(<span class="cm-variable">plus</span>(<span class="cm-variable">nine</span>())) <span class="cm-comment"># must return 13</span>
<span class="cm-variable">eight</span>(<span class="cm-variable">minus</span>(<span class="cm-variable">three</span>())) <span class="cm-comment"># must return 5</span>
<span class="cm-variable">six</span>(<span class="cm-variable">divided_by</span>(<span class="cm-variable">two</span>())) <span class="cm-comment"># must return 3</span>
</code></pre>
<p>Requirements:</p>
<ul>
<li>There must be a function for each number from 0 ("zero") to 9 ("nine")</li>
<li>There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (<code>divided_by</code> in Ruby and Python)</li>
<li>Each calculation consist of exactly one operation and two numbers</li>
<li>The most outer function represents the left operand, the most inner function represents the right operand</li>
<li>Division should be <strong>integer division</strong>. For example, this should return <code>2</code>, not <code>2.666666...</code>:</li>
</ul>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">eight</span>(<span class="cm-variable">dividedBy</span>(<span class="cm-variable">three</span>()));
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">eight</span>(<span class="cm-variable">divided_by</span>(<span class="cm-variable">three</span>))
</code></pre>
<pre><code class="language-python"><span class="cm-variable">eight</span>(<span class="cm-variable">divided_by</span>(<span class="cm-variable">three</span>()))
</code></pre>
</div>