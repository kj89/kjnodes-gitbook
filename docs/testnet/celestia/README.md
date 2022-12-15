# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: mocha | **Latest Version Tag**: v0.11.0 | **Wasm**: OFF

Website: [https://celestia.org](https://celestia.org)


## Public endpoints

* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@celestia-testnet.rpc.kjnodes.com:20656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@celestia-testnet.rpc.kjnodes.com:20659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/celestia-testnet/addrbook.json > $HOME/.celestia-app/config/addrbook.json
```

**live-peers** (7)
```
peers="f9e950870eccdb40e2386896d7b6a7687a103c99@88.99.219.120:43656,0d0f0e4a149b50a96207523a5408611dae2796b6@198.199.82.109:26656,43e9da043318a4ea0141259c17fcb06ecff816af@141.94.73.39:43656,c2870ce12cfb08c4ff66c9ad7c49533d2bd8d412@178.170.47.171:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,8bb8e34ac6eb4ddb927bb1cbbd44357683123af1@188.165.221.155:30542,e8906342e657ace92e1ed8599f0949da8dd75fbd@146.19.24.52:20656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.celestia-app/config/config.toml
```
