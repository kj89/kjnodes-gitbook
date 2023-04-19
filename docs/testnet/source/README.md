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
peers="2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,49b025c08193c8846956423ac80504b0bab2b777@185.182.187.239:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056,c27d26527c2f8a097c5a99800809d15338ac3bdb@95.217.207.236:20056,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:26976,da23ed57fc3d03b3864c309b589f2b5130a04a9f@65.109.111.204:28656,a21a9c2cf75ef23439e9bdcd6086ec47e7f614d7@159.69.155.107:25656,1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,503ec9be5c5542700b7f93d65dfc68371d38e6e9@16.163.74.176:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
