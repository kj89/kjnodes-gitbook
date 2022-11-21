# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-emerynet-5 | **Latest Version Tag**: pismoA | **Wasm**: OFF

Website: [https://agoric.com](https://agoric.com)


## Public endpoints

* rpc: [https://agoric-testnet.rpc.kjnodes.com](https://agoric-testnet.rpc.kjnodes.com)
* api: [https://agoric-testnet.api.kjnodes.com](https://agoric-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@agoric-testnet.rpc.kjnodes.com:27656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@agoric-testnet.rpc.kjnodes.com:27659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/agoric-testnet/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (10)
```
peers="793955daf95ad29f003cc4ec7e6c60c00677b2f7@5.9.81.187:30656,32f7fbecd40b420d592ac460703c4ac647875566@65.109.23.238:26656,42084028a65c5d609793ffc618d1dcbf374fc301@65.109.28.219:14456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:27656,fb86a0993c694c981a28fa1ebd1fd692f345348b@34.171.162.87:26656,98e1069b1cfc445e377eda6a0eadd94f7877065d@162.55.169.76:26656,a875ef614b3902dd567be2076f18239681f24e35@185.146.148.112:26656,bf32fb432cce9579c3bd20171f2918b9b2873796@154.12.225.46:26656,a5b991654d0723e038d3723b1345b2a288d49146@38.242.156.28:26656,6644a86094a0cb0152f83aed74357c439657770b@185.239.209.79:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
