<script>
    const path = window.location.hash.slice(1);
    export let item;    

    let item_id = path.slice(6);


</script>
<style>
    #detail {
        min-height: 420pt;
    }

    .loading {
        opacity: 0;
        animation: 0.4s 0.8s forwards fade-in;
    }

    @keyframes fade-in {
        from { opacity: 0; }
        to { opacity: 1; }
    }
</style>


<section id="detail" class="hero ">
    <div class="hero-body">
      <div class="container">
        <div class="columns">
          <div class="column is-8 is-offset-2">
          </div>
        </div>
        {#if item }
        <section class="section">
          <div class="columns">
            <div class="column is-10 is-offset-1">
              <div class="content is-medium">
                <h2 class="subtitle is-4">{item.date}</h2>
                <h1 class="title">{item.title}</h1>
                <p>{@html item.content}</p>
              </div>
           <a href="/#/home" class="">Back to home</a>
            </div>
          </div>
        </section>
        {:else}
         <p class="loading">Loading</p>
        {/if}
      </div>
    </div>
  </section>
