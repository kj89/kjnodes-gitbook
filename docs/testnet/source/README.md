# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" width="150" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: OFF

[Website](https://www.sourceprotocol.io/) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)



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

**live-peers** (20)
```bash
peers="b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,4466740c40895b6aad60a434f0ad3e3c5d5fe53c@213.239.216.252:22656,5a685935a69374c65c2fef0e61d31958cbf08614@213.239.215.77:22656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,7143126daf3c0983745a0b10b83c8e794c4fb2fc@65.108.126.46:33656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,ddb472d197b8a732bb3f8878035603769aa4c85b@161.35.75.82:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,4ede26dd5fbb87bd9dba462fe2c3c3e39e15c8f2@207.180.224.128:46656,829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,756368e62cbff16f8d0edcc4d169a090464bed53@38.242.194.233:26656,9f9d7c982cf37dd113192c6d4a5c4c0ac1997a25@185.22.152.217:26656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,148afdfb995b3aa727727a49c23324a804410a90@95.216.7.169:46656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,e36406628ec9d4ef1b231e412c98217d67216bca@65.109.122.105:60956,6e4cdcb3039f1f8e97b8511c3b146cd14d41dc3d@65.109.112.20:11084"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
