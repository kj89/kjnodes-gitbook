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

**live-peers** (14)
```bash
peers="1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,b57b9573b55c57c534cdb70a53138dec739b519d@212.23.222.220:26356,7a288e8d085b5aad8d43b0c6e6dbb8498588c206@5.182.17.164:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,da23ed57fc3d03b3864c309b589f2b5130a04a9f@65.109.111.204:28656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
