# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" width="150" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: OFF

[Website](https://www.sourceprotocol.io/) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)




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
peers="4466740c40895b6aad60a434f0ad3e3c5d5fe53c@213.239.216.252:22656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,4ede26dd5fbb87bd9dba462fe2c3c3e39e15c8f2@207.180.224.128:46656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,ddb472d197b8a732bb3f8878035603769aa4c85b@161.35.75.82:26656,c27d26527c2f8a097c5a99800809d15338ac3bdb@95.217.207.236:20056,756368e62cbff16f8d0edcc4d169a090464bed53@38.242.194.233:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,82d31c68dd604bbcd547eef014df465ee986b1d0@193.46.243.160:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,7143126daf3c0983745a0b10b83c8e794c4fb2fc@65.108.126.46:33656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
