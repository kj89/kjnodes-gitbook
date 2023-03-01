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
peers="935a9d809781aa4094dd806c2afed29a25ec8b8e@135.181.210.189:26656,d3796f3f2a179afab1485a672ace3d909cd0eeed@185.137.122.214:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,ad820cb2fa85e525538207bb24ee49a61a74eb45@93.115.25.15:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,da04ee3f8bd93421a3264e3a061a09c139aaa937@161.97.150.65:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,b5ce8fac0dd173d7154b3eb8d10136710e609d1e@95.216.21.37:29656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,5fde69fa32c6d509f920bedf1248c0c5f0369c14@15.165.223.141:26656,2af9f118d9be86892ef47193b6ab9e47046b9f44@74.207.231.41:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
