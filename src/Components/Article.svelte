<script>
    import { beforeUpdate } from "svelte";

    const PAGE_SIZE = 20;


    let items;

    $: fetch(`/index.json`)
        .then(r => r.json())
        .then(data => {
            items = data.sort(function(a,b){ return a.id-b.id}).reverse();
            window.scrollTo(0, 0);
        });
</script>

<style>
    #article{
        min-height: 420pt;
    }

    .loading {
        font-size: 30pt;
        opacity: 0;
        animation: 4.8s 0.1s forwards fade-in;
    }

    @keyframes fade-in {
        from { opacity: 0; }
        to { opacity: 1; }
    }
</style>


<section id="article" class="hero ">
    <div class="hero-body">
      <div class="container">
        <div class="columns">
          <div class="column is-10 is-offset-1">
          </div>
        </div>
        {#if items }
        {#each items as item, i}
        <section class="section">
          <div class="columns">
            <div class="column is-8 is-offset-2">
              <div class="content is-medium">
                <h2 class="subtitle is-4">{item.date}</h2>
                <h1 class="title">{item.title }</h1>
                <p>{item.content }</p>
                <a href="/#/item/{item.id}" class="button is-info">Read More</a>
              </div>
            </div>
          </div>
        </section>
        {/each}

        <div class="is-divider"></div>
        {:else}
            <section class="section has-text-centered">
                <h1 class="loading">Loading</h1>
            </section>
        {/if }
      </div>
    </div>
  </section>
