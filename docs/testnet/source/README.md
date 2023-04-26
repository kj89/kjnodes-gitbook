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
peers="4ede26dd5fbb87bd9dba462fe2c3c3e39e15c8f2@207.180.224.128:46656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,7ac1bce20b8ea73bb301201f446f2e6ae06f7ff6@65.109.104.118:61056,503ec9be5c5542700b7f93d65dfc68371d38e6e9@16.163.74.176:26656,2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656,b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,6d9cac37dfa58b8a13d59c85a8623f87138dd5ce@109.123.254.46:26656,756368e62cbff16f8d0edcc4d169a090464bed53@38.242.194.233:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
