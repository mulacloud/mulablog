<script>
    export let mode = "list";
	import { onMount } from 'svelte';
    import Header  from './Components/Header.svelte';
    import Article  from './Components/Article.svelte';
    import Detail  from './Components/Detail.svelte';
    import Footer from './Components/Footer.svelte';

    let item;
    let page;

    async function hashchange() {
        // the poor man's router!
        const path = window.location.hash.slice(1);

        if (path.startsWith('/item')) {
            const id = path.slice(6);
            item = await fetch(`/data/${id}.json`).then(r => r.json());
            window.scrollTo(0,0);
        } else if (path.startsWith('/top')) {
            page = +path.slice(5);
            item = null;
        } else {
            window.location.hash = '/top/1';
        }
    }

    onMount(hashchange);

</script>

<svelte:window on:hashchange={hashchange}/>

<main>
    <Header/>
    {#if item }
    <Detail {item}/>
    {:else if page }
    <Article/>
    {/if}
    <Footer/>
</main>

