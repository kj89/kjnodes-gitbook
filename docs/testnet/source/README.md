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
peers="2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,b57b9573b55c57c534cdb70a53138dec739b519d@212.23.222.220:26356,7ac1bce20b8ea73bb301201f446f2e6ae06f7ff6@65.109.104.118:61056,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,05dbcd1bb0563107c5eeb98a8da9d6cd9197bfcd@65.21.129.95:21756,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,2b2d05002f02cc480dd7dcf8f892ffca412cc451@149.102.139.49:39656,f6e7cb4ee4d608822802f58c85e93a7e34ce440d@65.108.237.232:28656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:26976,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
