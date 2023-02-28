# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.0-fix | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)




## Chain explorer
[https://explorer.kjnodes.com/bitcanna](https://explorer.kjnodes.com/bitcanna)

## Public endpoints

* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)
* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* grpc: [https://bitcanna.grpc.kjnodes.com](https://bitcanna.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:42656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (20)
```bash
peers="d27dc1222e9ab0d90e49490ee315797afa14a03f@65.108.99.254:27656,935a9d809781aa4094dd806c2afed29a25ec8b8e@135.181.210.189:26656,335c2b5099b4184e860939ec85d981e4ce036311@142.132.134.154:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,9532a13b05e5f68f2ca01f90b3d1ba9a762af817@65.108.131.190:21956,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,5fde69fa32c6d509f920bedf1248c0c5f0369c14@15.165.223.141:26656,5af4f132d1c63cbe9d828d58522fdbb4bd508880@136.244.29.116:31656,2af9f118d9be86892ef47193b6ab9e47046b9f44@74.207.231.41:26656,da04ee3f8bd93421a3264e3a061a09c139aaa937@161.97.150.65:26656,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
