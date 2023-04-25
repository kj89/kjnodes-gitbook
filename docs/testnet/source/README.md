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

**live-peers** (13)
```bash
peers="2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,e6a5db345775973982e32b24ba7f3bfa18337f66@65.108.124.219:33656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
