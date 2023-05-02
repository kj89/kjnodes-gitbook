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
peers="b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656,f22864303a45c1f22cdb00f8cfc7f914d18fce9c@135.181.20.30:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,6d9cac37dfa58b8a13d59c85a8623f87138dd5ce@109.123.254.46:26656,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,1b23b557898ae3221ae4cbd9ada3b1851ab09d6b@65.109.82.112:39656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,529d5e582ebf176a84df9698314037112d6061cc@207.180.212.166:26656,291a397d001fca8cf2991dfce8bc6f724d44295c@75.119.132.25:29656,8bf33f58eb977d2a3e8b3159e2949221201044d8@65.109.88.180:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
