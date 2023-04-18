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
peers="1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,c5eccf228a25f979592297311bfe2cc8ef94e482@95.111.229.159:26656,5f94cf456803179361c44c213fbc95f4da1bc3af@38.242.146.255:26656,42bb6ea45070248f5ea1d7c26db7665498a5b8c4@173.249.42.162:28656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,08e5694cbc077e361cc2e9daa7f91aa67797c92e@65.109.85.170:34656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,e2d9b74c65a383a34f9156adb47583e67f996a66@65.109.90.171:28656,80d48a1823db3c71f5e5babe89271156af6ceb89@194.163.156.184:26656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056,2c4a32763185e357c4a5e68a465bdc5375c7f413@136.243.88.91:3140,596112703a361a71e0c3dbf1b1b04f87e1c23e47@85.239.230.135:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
