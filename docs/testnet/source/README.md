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
* grpc: source-testnet.grpc.kjnodes.com:128090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:128656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:128659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (16)
```bash
peers="c5eccf228a25f979592297311bfe2cc8ef94e482@95.111.229.159:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,1c29673dc1fb273bffc55808a6118a61a08df830@65.108.151.10:26656,6d9cac37dfa58b8a13d59c85a8623f87138dd5ce@109.123.254.46:26656,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,148afdfb995b3aa727727a49c23324a804410a90@95.216.7.169:46656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,42bb6ea45070248f5ea1d7c26db7665498a5b8c4@173.249.42.162:28656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,1b23b557898ae3221ae4cbd9ada3b1851ab09d6b@65.109.82.112:39656,49b025c08193c8846956423ac80504b0bab2b777@185.182.187.239:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
