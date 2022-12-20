# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (34)
```
peers="02c20307295465ab2592fd81176e66be90d4bbe2@5.189.159.111:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,0eb70bf5e2403694109f9bba184570074c2dfdd5@38.242.235.255:26656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,a1e2432ca6f477619fd6a855f8798e6558f4599b@138.68.145.136:41656,b30d41820868f19784589dce150f07e3bdce8ea2@86.48.0.95:26656,85236d0c81cad2ce71c59b7aa7ab191bce545bff@89.117.50.45:656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,938ac1e4262cb2341bac323156fc3637f1b9c472@84.46.240.25:41656,deca8c5aed2d1e617789d80927394a1d4d1c7360@149.102.146.123:26656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,2f0484f05aa2d58d91aa21ea7cb9ce81c2e207ea@85.239.240.187:26656,ff4fab3a07cdf3601b90ececd2de9a85b3a1a42e@82.208.21.152:26656,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,b6651c7b043ef4bdccd7906b0f06de2bbdfe8a60@193.46.243.75:26656,0c37cd47e46901caadd8288a158edb81d37427a0@209.126.6.101:26656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,016b0e565abd496b9473b87ac41339251005d12e@194.163.167.163:41656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,6871aeacd353d66c38b1ebbf3b1ad244fa05e32b@167.86.84.125:26656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,3511b4bffe4d804065181625b32e2507934fdb05@82.208.20.137:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,e88708f6bda2af195f0ec48b9868e588ead964fb@144.91.82.239:26656,44a66336b029ba931165da3580cc6322af90339d@38.242.207.87:26656,19fb417249992ae8def277fb753656da318fe250@38.242.133.239:41656,965e495f4a69294bd85f3437fccdc9b210fd98b6@1.15.146.92:26656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,37c3d29df83da59e5a258d413e2f89365ab05711@85.239.243.12:656,5b599e2470b01f8afa88448899f436130fb2e2fd@146.190.112.167:26656,42ba206efd9dd10847fa20f09a74fde6706442aa@194.146.13.128:60956"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
