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
peers="49b025c08193c8846956423ac80504b0bab2b777@185.182.187.239:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,4ede26dd5fbb87bd9dba462fe2c3c3e39e15c8f2@207.180.224.128:46656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,b20497b3fb86603d04e00024766ec07dc3fe7e48@65.108.76.44:11563,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,63d1b126558468634137b5705ab90151b16932f8@65.108.151.6:26656,b4b37e3947ec2407a868929ef2788da3231bf6aa@161.35.154.141:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,1b794c9493f857ccce2eb800cf726f2cc4b42ebf@34.145.27.77:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,5a685935a69374c65c2fef0e61d31958cbf08614@213.239.215.77:22656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,4466740c40895b6aad60a434f0ad3e3c5d5fe53c@213.239.216.252:22656,829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
