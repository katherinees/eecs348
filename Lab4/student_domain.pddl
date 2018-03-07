(define (domain nosliw)
    (:requirements :strips :typing)
  (:types agent item location - default_object
        hero dragon wizard - agent
        sword pen diamond - item
        town mountain cave - location
        sorceress - wizard
  )
    (:predicates
  	    (at ?who ?where)
  	    (path-from-to ?from ?to)
        (possesses ?who ?what)
        (different ?a ?b)
        ;(magical ?who)
        (strong ?who)
        (asleep ?who)
        (dead ?who)
        (safe ?where)
        ;(hero ?h)
    )

    (:action inferdiff
        :parameters (?item1 - item ?item2 - item)
        :precondition (different ?item1 ?item2)
        :effect (and (different ?item1 ?item2)
                    (different ?item2 ?item1))
    )

    (:action travel
     	 :parameters (?who - hero ?from - location ?to - location)
     	 :precondition (and (at ?who ?from)
     	                    (path-from-to ?from ?to))
     	 :effect (and (not (at ?who ?from))
     	                (at ?who ?to))
    )

    (:action pickup
        :parameters (?who - hero ?what - item ?where - location)
        :precondition (and (at ?who ?where)
                            (at ?what ?where))
        :effect (and (possesses ?who ?what)
                    (not (at ?what ?where)))
    )

    (:action trade
        :parameters (?a - agent ?b - agent ?item1 - item ?item2 - item ?where - location)
        :precondition (and (possesses ?a ?item1)
                            (possesses ?b ?item2)
                            (at ?a ?where)
                            (at ?b ?where))
        :effect (and (not (possesses ?a ?item1))
                    (not (possesses ?b ?item2))
                    (possesses ?a ?item2)
                    (possesses ?b ?item1))
    )

    (:action drop
        :parameters (?a - hero ?obj - item ?where - location)
        :precondition (and (at ?a ?where)
                            (possesses ?a ?obj))
        :effect (and (not (possesses ?a ?obj))
                    (at ?obj ?where))
    )

    (:action magic
        :parameters (?m - wizard ?h - hero ?i1 - diamond ?i2 - diamond ?i3 - diamond ?where - location)
        :precondition (and (at ?m ?where)
                            (at ?h ?where)
                            (possesses ?h ?i1)
                            (possesses ?h ?i2)
                            (possesses ?h ?i3)
                            (different ?i1 ?i2)
                            (different ?i2 ?i3)
                            (different ?i3 ?i1))
                            ;(or (different ?i1 ?i2) (different ?i2 ?i1))
                            ;(or (different ?i2 ?i3) (different ?i3 ?i2))
                            ;(or (different ?i3 ?i1) (different ?i1 ?i3)))
        :effect (and (strong ?h)
                    (not (possesses ?h ?i1))
                    (not (possesses ?h ?i2))
                    (not (possesses ?h ?i3))
                    (possesses ?m ?i1)
                    (possesses ?m ?i2)
                    (possesses ?m ?i3))
    )

    (:action song
        :parameters (?h - hero ?quill - pen ?d - dragon ?hd - town)
        :precondition (and (possesses ?h ?quill)
                            (not (dead ?d)))
        :effect (and (asleep ?d)
                    (safe ?hd))
    )

    (:action slaying
        :parameters (?h - hero ?d - dragon ?s - sword ?cave - location ?hd - town)
        :precondition (and (at ?h ?cave)
                            (at ?d ?cave)
                            (strong ?h)
                            (possesses ?h ?s))
        :effect (and (dead ?d)
                    (not (asleep ?d))
                    (safe ?hd))
    )

)
