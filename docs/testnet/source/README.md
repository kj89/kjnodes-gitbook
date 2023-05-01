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
* grpc: source-testnet.grpc.kjnodes.com:12890

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:12856
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:12859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (19)
```bash
peers="b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,42bb6ea45070248f5ea1d7c26db7665498a5b8c4@173.249.42.162:28656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,86216a2e88322ca534fedaa91898272cc11d3cc9@173.249.23.196:28656,1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,6d9cac37dfa58b8a13d59c85a8623f87138dd5ce@109.123.254.46:26656,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,1709ae02a391357bad468987e208075ef53f969b@3.135.249.173:26656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,1b23b557898ae3221ae4cbd9ada3b1851ab09d6b@65.109.82.112:39656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
