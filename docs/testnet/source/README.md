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
peers="1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,63d1b126558468634137b5705ab90151b16932f8@65.108.151.6:26656,148afdfb995b3aa727727a49c23324a804410a90@95.216.7.169:46656,c749b47c438842d9874b515de130dfb11431360f@147.182.211.27:26656,3842f067439c4221e9f9535cdf59d22984d58fed@66.94.123.47:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,4466740c40895b6aad60a434f0ad3e3c5d5fe53c@213.239.216.252:22656,503ec9be5c5542700b7f93d65dfc68371d38e6e9@16.163.74.176:26656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,86216a2e88322ca534fedaa91898272cc11d3cc9@173.249.23.196:28656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,b4b37e3947ec2407a868929ef2788da3231bf6aa@161.35.154.141:26656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
