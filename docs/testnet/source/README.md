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

**live-peers** (15)
```bash
peers="4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,7ac1bce20b8ea73bb301201f446f2e6ae06f7ff6@65.109.104.118:61056,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:26976,1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,503ec9be5c5542700b7f93d65dfc68371d38e6e9@16.163.74.176:26656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056,3e16844d041df0f4b14d0d624fc94eadf50ed61d@65.108.13.154:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
