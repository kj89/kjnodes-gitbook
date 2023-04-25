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
peers="b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,6d9cac37dfa58b8a13d59c85a8623f87138dd5ce@109.123.254.46:26656,2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,503ec9be5c5542700b7f93d65dfc68371d38e6e9@16.163.74.176:26656,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
