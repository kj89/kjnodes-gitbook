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
peers="5a685935a69374c65c2fef0e61d31958cbf08614@213.239.215.77:22656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,b4b37e3947ec2407a868929ef2788da3231bf6aa@161.35.154.141:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,b20497b3fb86603d04e00024766ec07dc3fe7e48@65.108.76.44:11563,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,7143126daf3c0983745a0b10b83c8e794c4fb2fc@65.108.126.46:33656,0dd9790904c76aee0822dc766468dd67ba5ec0e7@51.81.57.80:10156,c749b47c438842d9874b515de130dfb11431360f@147.182.211.27:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,49b025c08193c8846956423ac80504b0bab2b777@185.182.187.239:26656,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,e6a5db345775973982e32b24ba7f3bfa18337f66@65.108.124.219:33656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
