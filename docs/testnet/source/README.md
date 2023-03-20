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
peers="4466740c40895b6aad60a434f0ad3e3c5d5fe53c@213.239.216.252:22656,829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,49b025c08193c8846956423ac80504b0bab2b777@185.182.187.239:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,6e4cdcb3039f1f8e97b8511c3b146cd14d41dc3d@65.109.112.20:11084,e6a5db345775973982e32b24ba7f3bfa18337f66@65.108.124.219:33656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656,b20497b3fb86603d04e00024766ec07dc3fe7e48@65.108.76.44:11563,da23ed57fc3d03b3864c309b589f2b5130a04a9f@65.109.111.204:28656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,0dd9790904c76aee0822dc766468dd67ba5ec0e7@51.81.57.80:10156,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,b4b37e3947ec2407a868929ef2788da3231bf6aa@161.35.154.141:26656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656,756368e62cbff16f8d0edcc4d169a090464bed53@38.242.194.233:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
