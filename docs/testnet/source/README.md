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

**live-peers** (11)
```bash
peers="2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,0dd9790904c76aee0822dc766468dd67ba5ec0e7@51.81.57.80:10156,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
