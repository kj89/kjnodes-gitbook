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
peers="49b025c08193c8846956423ac80504b0bab2b777@185.182.187.239:26656,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,829e2377df43a9f8e43ac6d886763c2a7b27a77c@195.2.93.179:26656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,4ede26dd5fbb87bd9dba462fe2c3c3e39e15c8f2@207.180.224.128:46656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,7143126daf3c0983745a0b10b83c8e794c4fb2fc@65.108.126.46:33656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656,b20497b3fb86603d04e00024766ec07dc3fe7e48@65.108.76.44:11563,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,ddb472d197b8a732bb3f8878035603769aa4c85b@161.35.75.82:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,b4b37e3947ec2407a868929ef2788da3231bf6aa@161.35.154.141:26656,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
