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
peers="4466740c40895b6aad60a434f0ad3e3c5d5fe53c@213.239.216.252:22656,ddb472d197b8a732bb3f8878035603769aa4c85b@161.35.75.82:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,291a397d001fca8cf2991dfce8bc6f724d44295c@75.119.132.25:29656,82d31c68dd604bbcd547eef014df465ee986b1d0@193.46.243.160:26656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,148afdfb995b3aa727727a49c23324a804410a90@95.216.7.169:46656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,5a685935a69374c65c2fef0e61d31958cbf08614@213.239.215.77:22656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,b20497b3fb86603d04e00024766ec07dc3fe7e48@65.108.76.44:11563,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
