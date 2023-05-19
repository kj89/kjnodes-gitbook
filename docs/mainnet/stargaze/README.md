# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" alt=""><figcaption></figcaption></figure>

Stargaze is a Cosmos zone (layer 1 proof-of-stake blockchain).  It is the base layer node software for the Stargaze NFT Marketplace.

**Chain ID**: stargaze-1 | **Latest Version Tag**: v9.0.0 | **Wasm**: ON

[Website](https://www.stargaze.zone) | [Discord](https://discord.gg/stargaze) | [Twitter](https://twitter.com/stargazezone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/stargaze](https://explorer.kjnodes.com/stargaze)

## Public endpoints

* api: [https://stargaze.api.kjnodes.com](https://stargaze.api.kjnodes.com)
* rpc: [https://stargaze.rpc.kjnodes.com](https://stargaze.rpc.kjnodes.com)
* grpc: stargaze.grpc.kjnodes.com:15890

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stargaze.rpc.kjnodes.com:15856
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stargaze.rpc.kjnodes.com:15859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stargaze/addrbook.json > $HOME/.starsd/config/addrbook.json
```

**live-peers** (9)
```bash
peers="7798342ae6f07e5c2e09bce8bab69e4485cacf64@5.9.72.212:3000,c2054e53fdb2f5cafb1a2f633de064143c16057c@93.189.30.126:26656,6f8eddb672e93eb3362a7cb1c843a4e26af71ebc@149.202.72.186:26629,fee838fe0381b3f74538a36d643991ceca3793c8@65.108.141.109:8656,d9307d7d7e219461ab9c333104780181b6933e74@89.58.50.116:26656,ce764e158a4a29a4af7606c38c44e976c69b3982@144.91.78.94:26656,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,06805bbbb45dbbcdadb963fda7f5b3733f331ebe@185.119.118.109:3000,56a776a589fbc4d038db956791bcf75204c67872@172.105.112.35:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
