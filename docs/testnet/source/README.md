# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" width="150" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://www.sourceprotocol.io) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: source-testnet.grpc.kjnodes.com:28090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:28656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:28659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (12)
```bash
peers="cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,8574b64414e446621dc9ad09bc25dd328cb6aa2d@184.174.37.152:28656,3e16844d041df0f4b14d0d624fc94eadf50ed61d@65.108.13.154:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
