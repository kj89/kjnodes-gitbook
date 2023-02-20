# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.5 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)




## Chain explorer
[https://explorer.kjnodes.com/uptick-testnet](https://explorer.kjnodes.com/uptick-testnet)

## Public endpoints

* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)
* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* grpc: [https://uptick-testnet.grpc.kjnodes.com](https://uptick-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (26)
```bash
peers="e8704845eaa0f3d39fcdc9c4065f3beb344384db@142.132.152.46:27656,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@94.23.23.189:6969,94734f927b16ff91f5e45875396295d6173ca918@74.50.70.118:11574,b1f4cbece3a83ea55ba28a50281eaa3af9119cd4@65.21.129.95:21256,967e0f06ad8b16dee6a8a6b8a48e8e5a63fdd810@178.211.139.225:7656,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,0aee682fb3453170737149203e5c23d2e0c46058@142.132.253.112:15656,0afdeea2f014bdfc43ab6dbdf567164daf861cf4@57.128.86.31:26656,c6ca186e2ea0202a78b357c9b2d8883e3d96613a@144.91.110.211:31656,00242af3dded97bb8380c9b9d98457ea7879e0c0@198.204.255.155:26656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,5739ae6fab71ec95fb3112f4d1ea2845782fa9f7@54.92.137.6:26656,7dace139a0389ca95c5eda64ddf19a01e6d60d02@95.214.52.206:26656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,6af07daddb8a57c01d05d8c0894f8293a41090d0@185.245.183.122:26656,883d6557bef1bae68c4fb569078caf0cf4c45bdd@142.132.202.50:26651,40ffd59440b11d63bfb8e20cfed5b36f282a06b3@154.12.238.247:31656,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,2c952455a0e425081b54855091ab84c1fe73c4bc@65.108.231.124:10656,bfc2be7e459b947973a15a01055cad86ad34f35c@185.163.127.24:15656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,75f90b4070eab7a20dc60974c85069389c77d89d@38.242.239.27:26656,7a9b1f1ed80e854dfbf95f921c35f950f9278ea4@161.97.162.123:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
