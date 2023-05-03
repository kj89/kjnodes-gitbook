# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/teritori.png" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-testnet-v3 | **Latest Version Tag**: v1.3.1 | **Wasm**: ON

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

**live-peers** (10)
```bash
peers="6bc9f80a5123d62c23aadb7b5d68b740a794b0c6@207.180.194.156:36656,ec0c58dbfe67a12ea16951134e29a6566ac05add@185.217.125.98:26656,31413c99357d0cfc48a46767ade171db2ea0205e@135.181.138.160:46656,bf100c1b6b44a6e96ab5691f3023cec3c27747fd@144.126.142.78:46656,5ae1012f9b0f4672d8152de903d115dd2f1a3ee3@65.21.170.3:27656,c56b132be41b247c9f8fa1f2addaca57f9946e29@75.119.159.159:44656,a2785cabecc10f591d9e8c396c8e162e95a206ec@65.108.226.183:15956,b9bd31a2a68a09d324a9deaf41144ff6d0dbe260@65.108.192.123:15656,3b539b6cff93fb3631d0a600a56ade3c6ca6bea3@162.19.236.64:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
