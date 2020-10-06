class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None                

    def find(self, key):
        cur_node = self.head
        
        while cur_node is not None: 
            # compare cur_node to key we're looking for
            if cur_node.key == key:
                return cur_node
            else: 
                cur_node = cur_node.next
        return None
    
    def insert_at_head(self, node):       
        # link node to current head
        node.next = self.head
        # set pointer to new node
        self.head = node

    def delete(self, key):
        # if node to del is head
        if key == self.head.key:
            self.head = self.head.next
            return self.head
        
        prev = None
        curr = self.head

        while curr is not None:
            # loop until right key is found
            if curr.key == key:
                prev.next = curr.next
                return curr
            #move pointers
            prev = curr
            curr = curr.next
        return None



# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = [MIN_CAPACITY] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.capacity)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Notes on LF: Load Factor is a measure that decides when to increase 
        # ht capacity to maintain get() & put() O(1) TC.
        # The default load factor is 0.75(75% of the ht volume / avail space)
        # So get_lf() needs to be a trigger to increase size once LF is > 0.75
        # Your code here
        # lf = .75
        lf = .7

        if lf >= self.capacity // self.get_num_slots():
            self.resize(self.capacity * 2)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # set var to 5381, this will be the hash multiplier
        # psuedocode:         
        # ht = self.capacity
        # for key in ht:
        #     hash_num = (( hash_num << 5) + hash_num) + ord(key)
        # return hash_num*ht        
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash         

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.get_num_slots()

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        self.key = key
        self.value = value
        if self.capacity[index] is not None:
            # search the ll for the node with the same key as what we are inserting
            if key == index:
            #  if it exists: 
                # change the value of the node 
                key = index
                index = index.next
                return key
            elif key != index: 
            # if it doesn't exist do the following:            
            # first item in the hash_array is HEAD of LL
            # Create a new hashtableentry & add to head of LL
            # make the new entry the new head
            # else:
                return HashTableEntry.insert_at_head(key, value)            
            # return
        self.capacity[index] = HashTableEntry(key, value)
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        return HashTableEntry.delete(self, key)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # index = self.hash_index(key)
        # Loop through the LL at the hashed index
        # compare the key to search to the key in the nodes
        # if you find it, return the value
        # if not, return None
        return HashTableEntry.find(self, key)


        # return self.capacity[index]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # Create new empty array w/ a new size
        # Doubling is standard
        # Items now need to be rehashed b/c the f() has changed 
            # iterate over each item in each ll
             #rehash the key in each item & store in new array

        # make new array with the new storage
        new_ht = HashTable(new_capacity)
        for key in self.capacity:
            value = self.get(key)
            new_ht.put(key, value)
        return new_ht



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
    
      

   
