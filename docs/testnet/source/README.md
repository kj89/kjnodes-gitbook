# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://www.sourceprotocol.io) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: source-testnet.grpc.kjnodes.com:12890

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:12856
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:12859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (11)
```bash
peers="854048fcfb453297742b76cc5c6b7555eeb25110@213.239.207.175:31656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,a833e9d068c7f5f32f411662c0430196a88aee91@65.109.65.248:28656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,08e5694cbc077e361cc2e9daa7f91aa67797c92e@65.109.85.170:34656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,e6a5db345775973982e32b24ba7f3bfa18337f66@65.108.124.219:33656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
