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
peers="1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,42bb6ea45070248f5ea1d7c26db7665498a5b8c4@173.249.42.162:28656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656,7ac1bce20b8ea73bb301201f446f2e6ae06f7ff6@65.109.104.118:61056,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,503ec9be5c5542700b7f93d65dfc68371d38e6e9@16.163.74.176:26656,651d2d055e44f4bdeb6904f94307fac42f21ec77@65.109.54.15:14656,7143126daf3c0983745a0b10b83c8e794c4fb2fc@65.108.126.46:33656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
