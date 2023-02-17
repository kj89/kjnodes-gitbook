# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/whitewhale.png" width="150" alt=""><figcaption></figcaption></figure>

Whitewhale is a Tendermint-based Interchain Liquidity.

**Chain ID**: migaloo-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://whitewhale.money) | [Discord](https://discord.gg/AyvcgD4jy3) | [Twitter](https://twitter.com/WhiteWhaleDefi)




## Chain explorer
[https://explorer.kjnodes.com/whitewhale](https://explorer.kjnodes.com/whitewhale)

## Public endpoints

* api: [https://whitewhale.api.kjnodes.com](https://whitewhale.api.kjnodes.com)
* rpc: [https://whitewhale.rpc.kjnodes.com](https://whitewhale.rpc.kjnodes.com)
* grpc: [https://whitewhale.grpc.kjnodes.com](https://whitewhale.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@whitewhale.rpc.kjnodes.com:49656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@whitewhale.rpc.kjnodes.com:49659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/whitewhale/addrbook.json > $HOME/.migalood/config/addrbook.json
```

**live-peers** (39)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:49656,6c42aacf3939d503bad695d86108d214680e04a8@144.76.175.189:20756,e39876398a43c0f9b93b5a82d8e38fa57c0373b5@65.109.89.19:20756,d8aa44568130ec24f953ce12708cb3ea72763cf5@88.208.241.28:26656,fe04ff9a13d8f0b23463e832f75eb5c845bd375e@213.239.214.73:7095,dfe5f91f824880e19d47475546d9874e0f2cea8c@5.79.74.229:8095,0c38efdc028867765e68f02979958468384ad087@51.89.155.2:23656,d20e91b12956469860da37a8e538305dad8d23d4@185.119.118.110:4000,4236750928a4dcb742e50e30e500ebc9ee39f240@35.223.246.103:26656,6801b2f80cdb6a02fbc7e23e1e1d393788e37e84@64.5.123.231:26656,2b9c4fd6be5b779417bc5bd392bdefc81a08720a@35.90.134.158:33656,81eefc4de6acec31ccdd519d53270be024e4fe68@51.210.223.186:7095,8ab347211b90560a0dca64ef0e4eef29012f2f67@65.109.71.119:26656,f4cada0792353a16093ea9ecb872cb5962ce01ce@65.109.71.210:26656,ccaccdf6bafcb57197d86a1420a289cd39fe0ae9@85.10.200.231:8095,41caa4106f68977e3a5123e56f57934a2d34a1c1@95.214.53.5:27096,554eb4a15e05af8317c3f98d6efd51d1ace1bc9c@146.59.85.223:20756,4f992b38332785ad794d52d936dc24792e719c9e@209.97.143.128:26656,1d3809b25bbe6a29bc2415df77c9fc82e46fd384@18.117.74.187:26656,ba6f2c1a1174fbc19e1fff75922f56c779d788d8@38.146.3.131:20756,5429bc670b77cd9c61481912ea194bea8aa6d0cd@51.81.155.189:20756,59c74642d0ec4d012dd7bd0a7e5af1eadf2061b2@65.109.30.183:26656,f7dede5bd05eb9615c8c6fa273e25bd4f10f56b8@65.108.109.240:3000,462a37ca052c4d058e505959393574045dce9489@116.202.36.240:20756,3b3428d679faa1bd498b3554ca798de3a0d802c6@162.19.89.8:20756,e91f650bb3d5b66762093150718af358c6355cc5@15.235.10.35:36656,d23d14793da108b107ac809f5643d5bbbbbcb6a5@65.108.75.107:46656,0326c9ee117587b7ebe3b26b00820642a8cf48ff@65.108.238.102:20756,4da079a17063c84724965a5367bbf8a52528dd67@65.108.128.139:2060,6870906f86e474d88d077c7c55af36debe49da04@178.162.165.194:7095,1efa54b5e318fad742f060d3938a963333bd8ae9@142.93.189.65:26656,0f1d4faac06ce19b964a7e5db063b328e58fdc6f@65.108.141.109:46656,23bbd46ad447ca81e78967892b4977ba4564f2d7@45.87.153.138:27656,9cb7ba30c7eb7e9b516b90e09ca0f53250927440@146.59.52.135:8095,aba0c3f98fb5bef1a0d991b8e2b8bba24f9908b6@65.108.111.236:55736,175ca82ab5b282549d68d79ff2c3703d26bcacef@141.94.109.71:20757,32eed8c4079201b143d92860c9146b1d9e126aa2@168.119.89.8:26656,347e6fa3c974e91aee92da5793486ba3f1bae67d@23.88.112.67:26656,80be85c4980deccaa2fbd710029f0eb660dadf9a@51.81.16.186:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.migalood/config/config.toml
```
