# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/teritori.png" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-testnet-v3 | **Latest Version Tag**: v1.4.0 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/teritori-testnet](https://explorer.kjnodes.com/teritori-testnet)

## Public endpoints

* api: [https://teritori-testnet.api.kjnodes.com](https://teritori-testnet.api.kjnodes.com)
* rpc: [https://teritori-testnet.rpc.kjnodes.com](https://teritori-testnet.rpc.kjnodes.com)
* grpc: teritori-testnet.grpc.kjnodes.com:11990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@teritori-testnet.rpc.kjnodes.com:11956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@teritori-testnet.rpc.kjnodes.com:11959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/teritori-testnet/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (8)
```bash
peers="a2785cabecc10f591d9e8c396c8e162e95a206ec@65.108.226.183:15956,3614bc766d73bebf6b73737b6690af60e7f0683e@65.108.206.118:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11956,ec0c58dbfe67a12ea16951134e29a6566ac05add@185.217.125.98:26656,31413c99357d0cfc48a46767ade171db2ea0205e@135.181.138.160:46656,4ebfdac0d496be2407c02202e5ad6f226a11b37a@65.21.134.202:26736,b33ebb4672f929dddde1365c9678a39abfd881fb@54.202.144.51:26656,15dd94f68c450da2c3b7c60b6364e3dce6f0cbf2@185.193.66.68:26641"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
