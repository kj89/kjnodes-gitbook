# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" alt=""><figcaption></figcaption></figure>

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
peers="2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,6d9cac37dfa58b8a13d59c85a8623f87138dd5ce@109.123.254.46:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
