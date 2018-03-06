(define (domain nosliw)
    (:requirements :strips :typing)
  (:types agent item location - default_object
        hero dragon sorceress wizard - agent
        sword pen diamond - item
        town mountain cave - location
  )
    (:predicates
  	    (at ?where ?who)
  	    (path-from-to ?from ?to)
        (possesses ?who ?what)
        (different ?a ?b)
        (hero ?h)
    )

    (:action travel
     	 :parameters (?who - hero ?from - location ?to - location)
     	 :precondition (and (at ?who ?from)
     	                    (path-from-to ?from ?to))
     	 :effect (and (not (at ?who ?from))
     	                (at ?who ?to))
    )

    (:action pickup
        :parameters (?who - agent ?what - location ?where - location)
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

)
