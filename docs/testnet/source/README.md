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

**live-peers** (16)
```bash
peers="8574b64414e446621dc9ad09bc25dd328cb6aa2d@184.174.37.152:28656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656,7a288e8d085b5aad8d43b0c6e6dbb8498588c206@5.182.17.164:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:26976,2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,c5eccf228a25f979592297311bfe2cc8ef94e482@95.111.229.159:26656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056,3e16844d041df0f4b14d0d624fc94eadf50ed61d@65.108.13.154:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
