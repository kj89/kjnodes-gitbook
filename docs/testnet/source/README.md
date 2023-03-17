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
peers="4466740c40895b6aad60a434f0ad3e3c5d5fe53c@213.239.216.252:22656,ddb472d197b8a732bb3f8878035603769aa4c85b@161.35.75.82:26656,829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,4ede26dd5fbb87bd9dba462fe2c3c3e39e15c8f2@207.180.224.128:46656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,6e4cdcb3039f1f8e97b8511c3b146cd14d41dc3d@65.109.112.20:11084,148afdfb995b3aa727727a49c23324a804410a90@95.216.7.169:46656,b20497b3fb86603d04e00024766ec07dc3fe7e48@65.108.76.44:11563,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,63d1b126558468634137b5705ab90151b16932f8@65.108.151.6:26656,9f9d7c982cf37dd113192c6d4a5c4c0ac1997a25@185.22.152.217:26656,3842f067439c4221e9f9535cdf59d22984d58fed@66.94.123.47:26656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,c749b47c438842d9874b515de130dfb11431360f@147.182.211.27:26656,291a397d001fca8cf2991dfce8bc6f724d44295c@75.119.132.25:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
